#!/usr/bin/env python

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import time
from functools import cached_property
from threading import Event, Thread
from typing import Any

import numpy as np
import rtde_control
import rtde_receive
from scipy.spatial.transform import Rotation as R

from lerobot.cameras.utils import make_cameras_from_configs
from lerobot.robots.robot import Robot

from .config_ur5e import UR5eConfig

logger = logging.getLogger(__name__)


class UR5e(Robot):
    """
    Universal Robots UR5e manipulator with Robotiq gripper and RealSense cameras.
    Uses RTDE (Real-Time Data Exchange) protocol for direct robot control.
    """

    config_class = UR5eConfig
    name = "ur5e"

    def __init__(self, config: UR5eConfig):
        super().__init__(config)
        self.config = config
        self.num_dofs = 7  # 6 joints + 1 gripper
        self.num_tcp_dofs = 7  # x, y, z, rx, ry, rz + gripper

        # Initialize RTDE interfaces
        logger.info(f"Connecting to UR5e at {config.robot_ip}")
        self.robot = rtde_control.RTDEControlInterface(config.robot_ip)
        self.r_inter = rtde_receive.RTDEReceiveInterface(config.robot_ip)

        # Initialize gripper
        if config.use_gripper:
            from .robotiq import CtrlGrp

            logger.info(f"Initializing Robotiq gripper on {config.gripper_port}")
            self.gripper = CtrlGrp(config.gripper_port)
            self.gripper.ACT()  # Activate gripper (blocking)
            time.sleep(1)
            self.last_gripper_pos = self._get_gripper_pos()
            self.last_gripper_command = self.last_gripper_pos
            self.start_gripper_thread()

        # Disable freedrive mode
        self._free_drive = False
        self.robot.endFreedriveMode()

        # Track last commands for safety checks
        self._last_joint_command = None
        self._last_tcp_command = None

        # Move to home position
        if config.init:
            logger.info("Moving to home pose...")
            self.rest_home_pose()

        # Initialize cameras
        logger.info("Initializing cameras...")
        self.cameras = make_cameras_from_configs(config.cameras)

    def start_gripper_thread(self):
        """Start background thread for gripper control at 120 Hz."""
        self.stop_event = Event()
        self.thread = Thread(
            target=self.run_gripper_loop, name="ur5e_gripper_loop"
        )
        self.thread.daemon = True
        self.thread.start()

    def run_gripper_loop(self):
        """Background loop for gripper control and feedback."""
        fps = 120
        while not self.stop_event.is_set():
            start_time = time.time()

            # Send gripper command (0-255 range)
            self.gripper.GTO([int(self.last_gripper_command * 255), 255, 255])

            # Read gripper position
            self.last_gripper_pos = self._get_gripper_pos()

            # Precise timing
            elapsed = time.time() - start_time
            sleep_time = max(0, 1 / fps - elapsed)
            time.sleep(sleep_time)

    def rest_home_pose(
        self, init_joint_position: np.ndarray = None, init_tcp_position: np.ndarray = None
    ):
        """Move robot to home position with smooth interpolation."""
        assert (
            init_joint_position is None or init_tcp_position is None
        ), "You can only set one of the two"

        if init_joint_position is None and init_tcp_position is None:
            if self.config.init_method == "joint":
                init_joint_position = self.config.init_joint_positions
            elif self.config.init_method == "tcp":
                init_tcp_position = self.config.init_tcp_positions
            else:
                raise NotImplementedError("Unknown initialization method")

        obs = self.get_observation(use_camera=False)

        if init_joint_position is not None:
            # Joint space interpolation
            curr_joints = obs["joint_positions"]
            reset_joints = np.array(init_joint_position)

            if reset_joints.shape == curr_joints.shape:
                delta = np.abs(curr_joints - reset_joints)
                if delta.shape[0] == 7:
                    max_delta = delta[:-1].max()  # Exclude gripper
                else:
                    max_delta = delta.max()
                steps = min(int(max_delta / 0.01), 25)

                for jnt in np.linspace(curr_joints, reset_joints, steps):
                    self.step_joint(jnt)
                    time.sleep(0.05)
            else:
                raise ValueError(
                    f"Initial joint position has wrong shape, got {reset_joints.shape}, expected {curr_joints.shape}"
                )

        elif init_tcp_position is not None:
            # TCP space interpolation
            curr_tcp = obs["ee_pos_rot"]
            reset_tcp = np.array(init_tcp_position)

            if reset_tcp.shape == curr_tcp.shape:
                max_delta = (np.abs(curr_tcp - reset_tcp)).max()
                steps = min(int(max_delta / 0.01), 25)

                for tcp in np.linspace(curr_tcp, reset_tcp, steps):
                    self.step_tcp(tcp)
                    time.sleep(0.05)
            else:
                raise ValueError(
                    f"Initial tcp position has wrong shape, got {reset_tcp.shape}, expected {curr_tcp.shape}"
                )

    @cached_property
    def observation_features(self) -> dict[str, type | tuple]:
        """Define observation space features."""
        features = {}

        # Joint states (7D: 6 joints + 1 gripper)
        for i in range(self.num_dofs):
            features[f"joint_positions_{i}"] = float

        # TCP states (7D: xyz + rotvec + gripper)
        for i in range(self.num_tcp_dofs):
            features[f"ee_pos_rot_{i}"] = float

        # Camera images (height, width, channels)
        for cam_name, cam_config in self.config.cameras.items():
            features[cam_name] = (cam_config.height, cam_config.width, 3)

        return features

    @cached_property
    def action_features(self) -> dict[str, type]:
        """Define action space features."""
        features = {}

        # Joint actions (7D)
        for i in range(self.num_dofs):
            features[f"joint_positions_{i}"] = float

        # TCP actions (7D)
        for i in range(self.num_tcp_dofs):
            features[f"ee_pos_rot_{i}"] = float

        return features

    def get_observation(self, use_camera=True) -> dict[str, Any]:
        """
        Get current observation including images, joint states, and TCP pose.

        Args:
            use_camera: Whether to include camera images

        Returns:
            Dictionary with observation data
        """
        obs_dict = {}

        # 1. Read camera images
        if use_camera:
            for cam_name, cam_instance in self.cameras.items():
                obs_dict[cam_name] = cam_instance.read()

        # 2. Get TCP state (6D: xyz + rotvec)
        robot_tcp = self.r_inter.getActualTCPPose()  # [x, y, z, rx, ry, rz]

        # 3. Get joint state (6D)
        robot_joints = self.r_inter.getActualQ()  # [q0, q1, q2, q3, q4, q5]

        # 4. Add gripper state
        if self.config.use_gripper:
            gripper_pos = self.last_gripper_pos
            obs_dict["ee_pos_rot"] = np.append(robot_tcp, gripper_pos)
            obs_dict["joint_positions"] = np.append(robot_joints, gripper_pos)
        else:
            obs_dict["ee_pos_rot"] = robot_tcp
            obs_dict["joint_positions"] = robot_joints

        # 5. Flatten to individual keys (required by LeRobot)
        for i in range(len(obs_dict["ee_pos_rot"])):
            obs_dict[f"ee_pos_rot_{i}"] = obs_dict["ee_pos_rot"][i]

        for i in range(len(obs_dict["joint_positions"])):
            obs_dict[f"joint_positions_{i}"] = obs_dict["joint_positions"][i]

        return obs_dict

    def send_action(self, action: dict[str, Any], action_type="joint") -> dict[str, Any]:
        """
        Send action to robot.

        Args:
            action: Dictionary with action values
            action_type: Control mode ("joint" or "tcp")

        Returns:
            Dictionary with new observation
        """
        # Choose control method based on action_type or config
        if action_type == "joint" or self.config.control_method == "joint":
            joint_action = np.array(
                [action[f"joint_positions_{i}"] for i in range(self.num_dofs)]
            )
            self.step_joint(joint_action)

        elif action_type == "tcp" or self.config.control_method == "tcp":
            tcp_action = np.array([action[f"ee_pos_rot_{i}"] for i in range(self.num_tcp_dofs)])
            self.step_tcp(tcp_action)

        else:
            raise ValueError(f"Unknown action_type: {action_type}")

        # Return new observation
        return self.get_observation()

    def step_joint(self, joint_state: np.ndarray) -> None:
        """
        Command robot to joint positions using servoJ.

        Args:
            joint_state: Target joint positions (7D: 6 joints + gripper)
        """
        # Safety check
        self.check_safety_joint(joint_state)

        # RTDE control parameters
        velocity = 0.5  # rad/s
        acceleration = 0.5  # rad/s²
        dt = 1.0 / 500  # 500 Hz control loop
        lookahead_time = 0.2
        gain = 100

        # Extract robot joints (first 6)
        robot_joints = joint_state[:6]

        # Send RTDE command
        t_start = self.robot.initPeriod()
        self.robot.servoJ(robot_joints, velocity, acceleration, dt, lookahead_time, gain)
        self.robot.waitPeriod(t_start)

        # Update gripper command (executed asynchronously by thread)
        if self.config.use_gripper:
            gripper_pos = self.process_gripper_pos(joint_state[-1])
            self.last_gripper_command = gripper_pos

        # Track last command
        self._last_joint_command = joint_state

    def step_tcp(self, tcp_state: np.ndarray) -> None:
        """
        Command robot to TCP pose using servoL.

        Args:
            tcp_state: Target TCP pose (7D: x, y, z, rx, ry, rz, gripper)
        """
        # RTDE control parameters (same as joint control)
        velocity = 0.5
        acceleration = 0.5
        dt = 1.0 / 500
        lookahead_time = 0.2
        gain = 100

        # Extract TCP pose (first 6: x, y, z, rx, ry, rz)
        robot_tcp = tcp_state[:6]

        # Send RTDE command
        t_start = self.robot.initPeriod()
        self.robot.servoL(robot_tcp, velocity, acceleration, dt, lookahead_time, gain)
        self.robot.waitPeriod(t_start)

        # Update gripper
        if self.config.use_gripper:
            gripper_pos = self.process_gripper_pos(tcp_state[-1])
            self.last_gripper_command = gripper_pos

        # Track last command
        self._last_tcp_command = tcp_state

    def check_safety_joint(self, action: np.ndarray) -> np.ndarray:
        """
        Check if joint delta exceeds safety limit (0.5 rad).

        Args:
            action: Target joint positions

        Returns:
            Modified action (with angle wrapping)

        Raises:
            ValueError: If delta exceeds safety limit
        """
        joint_positions = self.get_joint_state()

        # Calculate delta (handle angle wrapping)
        deltas = (action - joint_positions)[:6]
        deltas = (deltas + np.pi) % (2 * np.pi) - np.pi  # Normalize to [-π, π]
        action[:6] = joint_positions[:6] + deltas

        # Check maximum delta
        abs_deltas = np.abs(deltas)
        abs_deltas = np.minimum(abs_deltas % (2 * np.pi), 2 * np.pi - (abs_deltas % (2 * np.pi)))

        max_joint_delta = 0.5  # rad
        if abs_deltas.max() > max_joint_delta:
            # Log violations
            id_mask = abs_deltas > max_joint_delta
            ids = np.arange(len(id_mask))[id_mask]
            for i in ids:
                logger.error(
                    f"Joint[{i}] delta={abs_deltas[i]:.3f} exceeds limit "
                    f"(target={action[i]:.3f}, current={joint_positions[i]:.3f})"
                )
            raise ValueError(
                f"Joint delta exceeds safety limit: {abs_deltas.max():.3f} > {max_joint_delta}"
            )

        return action

    def process_gripper_pos(self, command: float) -> float:
        """
        Process gripper position command.

        Args:
            command: Gripper position in meters

        Returns:
            Normalized gripper position (0-1)
        """
        # Convert from meters to 0-1 range
        command = (command - self.config.gripper_limits[0]) / (
            self.config.gripper_limits[1] - self.config.gripper_limits[0]
        )
        command = max(min(command, 1.0), 0.0)

        # Optional binarization
        if self.config.binarize_gripper:
            command = 1.0 if command >= self.config.gripper_threshold else 0.0

        return command

    def _get_gripper_pos(self) -> float:
        """
        Read gripper position from Robotiq gripper.

        Returns:
            Normalized gripper position (0-1)
        """
        status = self.gripper.OBJ()  # Returns (status, position, position_mm)
        pos = status[1] / 255.0  # Normalize to 0-1
        return pos

    def get_joint_state(self, use_command=False) -> np.ndarray:
        """
        Get current joint state.

        Args:
            use_command: If True, return last commanded position

        Returns:
            Joint positions (7D: 6 joints + gripper)
        """
        if use_command and self._last_joint_command is not None:
            return self._last_joint_command
        else:
            joints = self.r_inter.getActualQ()
            if self.config.use_gripper:
                return np.append(joints, self.last_gripper_pos)
            return joints

    def get_tcp_state(self, use_command=False) -> np.ndarray:
        """
        Get current TCP state.

        Args:
            use_command: If True, return last commanded pose

        Returns:
            TCP pose (7D: x, y, z, rx, ry, rz, gripper)
        """
        if use_command and self._last_tcp_command is not None:
            return self._last_tcp_command
        else:
            tcp = self.r_inter.getActualTCPPose()
            if self.config.use_gripper:
                return np.append(tcp, self.last_gripper_pos)
            return tcp

    def connect(self, calibrate: bool = True) -> None:
        """Connect cameras."""
        for cam in self.cameras.values():
            cam.connect()

    @property
    def is_connected(self) -> bool:
        """RTDE connection is established in __init__."""
        return True

    def disconnect(self):
        """Disconnect and stop gripper thread."""
        if hasattr(self, "stop_event"):
            self.stop_event.set()
        if hasattr(self, "thread"):
            self.thread.join(timeout=2.0)
        # RTDE interfaces are automatically closed

    @property
    def is_calibrated(self) -> bool:
        """UR robots are factory calibrated."""
        return True

    def calibrate(self) -> None:
        """No manual calibration needed for UR robots."""
        pass
