import logging
import time
from typing import Any

import numpy as np
from threading import Event, Thread

from .config import URConfig

logger = logging.getLogger(__name__)


class UR:
    """Single UR arm control via RTDE + optional Robotiq gripper."""

    def __init__(self, config: URConfig):
        import rtde_control
        import rtde_receive

        self.config = config
        self.num_dofs = 7
        self.num_tcp_dofs = 7
        self.robot = rtde_control.RTDEControlInterface(config.robot_ip)
        self.r_inter = rtde_receive.RTDEReceiveInterface(config.robot_ip)

        if config.use_gripper:
            from .robotiq import CtrlGrp
            self.gripper = CtrlGrp(config.gripper_port)
            self.gripper.ACT()
            time.sleep(1)
            self.last_gripper_pos = self._get_gripper_pos()
            self.last_gripper_command = self.last_gripper_pos
            self._start_gripper_thread()

        self._free_drive = False
        self.robot.endFreedriveMode()

        if config.init:
            print("Go to home pose")
            self.rest_home_pose()

    def _start_gripper_thread(self):
        self.stop_event = Event()
        self.thread = Thread(target=self._run_gripper_loop, daemon=True)
        self.thread.start()

    def _run_gripper_loop(self):
        fps = 120
        while not self.stop_event.is_set():
            start_time = time.time()
            self.gripper.GTO([int(self.last_gripper_command * 255), 255, 255])
            self.last_gripper_pos = self._get_gripper_pos()
            elapsed = time.time() - start_time
            time.sleep(max(0, 1 / fps - elapsed))

    def process_gripper_pos(self, command):
        command = (command - self.config.gripper_limits[0]) / (self.config.gripper_limits[1] - self.config.gripper_limits[0])
        command = max(min(command, 1.0), 0.0)
        if self.config.binarize_gripper:
            command = 1.0 if command >= self.config.gripper_threshold else 0.0
        return command

    def _get_gripper_pos(self) -> float:
        gripper_pos = self.gripper.OBJ()[1] / 255
        gripper_pos = self.process_gripper_pos(gripper_pos)
        return gripper_pos

    def get_tcp_state(self, use_command=False) -> np.ndarray:
        robot_tcp = self.r_inter.getActualTCPPose()
        if self.config.use_gripper:
            gripper_pos = self.last_gripper_command if use_command else self.last_gripper_pos
            pos = np.append(robot_tcp, gripper_pos)
        else:
            pos = np.array(robot_tcp)
        return np.array(pos)

    def get_joint_state(self, use_command=False) -> np.ndarray:
        robot_joints = self.r_inter.getActualQ()
        if self.config.use_gripper:
            gripper_pos = self.last_gripper_command if use_command else self.last_gripper_pos
            pos = np.append(robot_joints, gripper_pos)
        else:
            pos = np.array(robot_joints)
        return np.array(pos)

    def step_joint(self, joint_state: np.ndarray) -> None:
        self.check_safety_joint(joint_state)
        velocity = 0.5
        acceleration = 0.5
        dt = 1.0 / 500
        lookahead_time = 0.2
        gain = 100

        robot_joints = joint_state[:6]
        t_start = self.robot.initPeriod()
        self.robot.servoJ(robot_joints, velocity, acceleration, dt, lookahead_time, gain)
        if self.config.use_gripper:
            self.last_gripper_command = self.process_gripper_pos(joint_state[-1])
        self.robot.waitPeriod(t_start)

    def step_tcp(self, tcp_state: np.ndarray) -> None:
        velocity = 0.5
        acceleration = 0.5
        dt = 1.0 / 500
        lookahead_time = 0.2
        gain = 100

        robot_tcp = tcp_state[:6]
        t_start = self.robot.initPeriod()
        self.robot.servoL(robot_tcp, velocity, acceleration, dt, lookahead_time, gain)
        if self.config.use_gripper:
            self.last_gripper_command = self.process_gripper_pos(tcp_state[-1])
        self.robot.waitPeriod(t_start)

    def rest_home_pose(self, init_joint_position=None):
        if init_joint_position is None:
            init_joint_position = self.config.init_joint_positions

        curr_joints = self.get_joint_state()
        reset_joints = np.array(init_joint_position)

        if reset_joints.shape != curr_joints.shape:
            raise ValueError(f"Initial joint position shape mismatch: {reset_joints.shape} vs {curr_joints.shape}")

        delta = np.abs(curr_joints - reset_joints)
        max_delta = delta[:-1].max() if delta.shape[0] == 7 else delta.max()
        steps = min(int(max_delta / 0.01), 25)

        for jnt in np.linspace(curr_joints, reset_joints, steps):
            self.step_joint(jnt)
            time.sleep(0.05)

    def check_safety_joint(self, action: np.ndarray) -> np.ndarray:
        joint_positions = self.get_joint_state()
        deltas = (action - joint_positions)[:6]
        deltas = (deltas + np.pi) % (2 * np.pi) - np.pi
        action[:6] = joint_positions[:6] + deltas

        abs_deltas = np.abs(deltas)
        abs_deltas = np.minimum(abs_deltas % (2 * np.pi), 2 * np.pi - (abs_deltas % (2 * np.pi)))
        max_joint_delta = 0.8
        if abs_deltas.max() > max_joint_delta:
            id_mask = abs_deltas > max_joint_delta
            ids = np.arange(len(id_mask))[id_mask]
            for i, delta, joint, current_j in zip(
                ids, abs_deltas[id_mask], action[:6][id_mask], joint_positions[:6][id_mask]
            ):
                print(f"joint[{i}]: delta: {delta:.3f}, target: {joint:.3f}, current: {current_j:.3f}")
            raise ValueError("Joint delta too large")
        return action

    def disconnect(self):
        if hasattr(self, "stop_event"):
            self.stop_event.set()
        if hasattr(self, "thread"):
            self.thread.join()
