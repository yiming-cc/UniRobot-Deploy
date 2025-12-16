
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

# TODO(aliberts, Steven, Pepijn): use gRPC calls instead of zmq?

import base64
import json
import logging
from functools import cached_property
from typing import Any
import time 

import cv2
import numpy as np
import torch

from lerobot.errors import DeviceAlreadyConnectedError, DeviceNotConnectedError
from lerobot.find_cameras import create_camera_instance, find_and_print_cameras, process_camera_image
from lerobot.cameras.utils import make_cameras_from_configs

from ..robot import Robot
from .config_ur import UR30Config, UR30BimanualConfig
from scipy.spatial.transform import Rotation as R
from gello.zmq_core.robot_node import ZMQClientRobot

def rvec_to_R(rvec):
    rotation = R.from_rotvec(rvec)
    return rotation.as_matrix()

def R_to_rvec(rot_matrix):
    rotation = R.from_matrix(rot_matrix)
    return rotation.as_rotvec()

def Rx(a):
    ca, sa = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0],
                     [0, ca, -sa],
                     [0, sa,  ca]])

def Ry(a):
    ca, sa = np.cos(a), np.sin(a)
    return np.array([[ ca, 0, sa],
                     [  0, 1,  0],
                     [-sa, 0, ca]])

def Rz(a):
    ca, sa = np.cos(a), np.sin(a)
    return np.array([[ca, -sa, 0],
                     [sa,  ca, 0],
                     [ 0,   0, 1]])

class UR30(Robot):
    config_class = UR30Config
    name = "ur30"

    def __init__(self, config: UR30Config):
        super().__init__(config)
        self.num_dofs = 7
        self.num_tcp_dofs = 7
        self.config = config
        
        self.robot = ZMQClientRobot(port=config.zmq_port, host="127.0.0.1")
        if config.init:
            print("Go to home pose")
            self.rest_home_pose()
        self.cameras = make_cameras_from_configs(config.cameras)

        if not self.cameras:
            logging.warning("No cameras could be connected. Aborting image save.")
        
    def rest_home_pose(self, init_joint_position: np.ndarray = None, init_tcp_position: np.ndarray = None):
        assert init_joint_position is None or init_tcp_position is None, "You can only set one of the two"
        if init_joint_position is None and init_tcp_position is None:
            if self.config.init_method == 'joint':
                init_joint_position = self.config.init_joint_positions
            elif self.config.init_method == 'tcp':
                init_tcp_position = self.config.init_tcp_positions
            else:
                raise NotImplementedError("Unknown initialization method")
        obs = self.get_observation(use_camera=False)
        if init_joint_position is not None:
            curr_joints = obs["joint_positions"]
            reset_joints = np.array(init_joint_position)
            if reset_joints.shape == curr_joints.shape:
                max_delta = (np.abs(curr_joints - reset_joints)).max()
                steps = min(int(max_delta / 0.01), 25)

                for jnt in np.linspace(curr_joints, reset_joints, steps):
                    self.step_joint(jnt)
                    time.sleep(0.05)
            else:
                raise ValueError(f"Initial joint position has wrong shape, got {reset_joints.shape}, expected {curr_joints.shape}")
        elif init_tcp_position is not None:
            curr_tcp = obs["ee_pos_rot"]
            reset_tcp = np.array(init_tcp_position)
            if reset_tcp.shape == curr_tcp.shape:
                max_delta = (np.abs(curr_tcp - reset_tcp)).max()
                steps = min(int(max_delta / 0.01), 25)

                for tcp in np.linspace(curr_tcp, reset_tcp, steps):
                    self.step_tcp(tcp)
                    time.sleep(0.001)
            else:
                raise ValueError(f"Initial tcp position has wrong shape, got {reset_tcp.shape}, expected {curr_tcp.shape}")
            
    @cached_property
    def _state_ft(self) -> dict[str, type]:
        keys = [f"ee_pos_rot_{i}" for i in range(7)] + \
                [f"joint_positions_{i}" for i in range(7)]
        # keys = [f"joint_positions_{i}" for i in range(7)]
        # keys = [f"ee_pos_rot_{i}" for i in range(7)]
        # keys = [f"ee_pos_rot_{i}" for i in range(7)] + \
        #         [f"joint_positions_{i}" for i in range(7)] + \
        #         [f"joint_velocities_{i}" for i in range(7)]
        # keys = [f"ee_pos_rot_{i}" for i in range(self.num_tcp_dofs)] + \
        #         [f"joint_positions_{i}" for i in range(self.num_dofs)]
        # keys = [f"joint_positions_{i}" for i in range(self.num_dofs)]
        
        return dict.fromkeys(keys, float)
            
    
    @cached_property
    def _action_ft(self) -> dict[str, type]:
        keys = [f"ee_pos_rot_{i}" for i in range(self.num_tcp_dofs)]+[f"joint_positions_{i}" for i in range(self.num_dofs)]
        # keys = [f"ee_pos_rot_{i}" for i in range(self.num_tcp_dofs)]
        # keys = [f"joint_positions_{i}" for i in range(self.num_dofs)]
        
        return dict.fromkeys(keys, float)

    @cached_property
    def _state_order(self) -> tuple[str, ...]:
        return tuple(self._state_ft.keys())

    @cached_property
    def _cameras_ft(self) -> dict[str, tuple[int, int, int]]:
        return {name: (cfg.height, cfg.width, 3) for name, cfg in self.config.cameras.items()}

    @cached_property
    def observation_features(self) -> dict[str, type | tuple]:
        return {**self._state_ft, **self._cameras_ft}

    @cached_property
    def action_features(self) -> dict[str, type]:
        return self._action_ft

    @property
    def is_connected(self) -> bool:
        return True

    @property
    def is_calibrated(self) -> bool:
        pass

    def connect(self) -> None:
        """Establishes ZMQ sockets with the remote mobile robot"""

        for cam in self.cameras.values():
            cam.connect()

        return True

    def calibrate(self) -> None:
        pass

    def get_observation(self, use_camera=True) -> dict[str, Any]:
        """
        Capture observations from the remote robot: current follower arm positions,
        present wheel speeds (converted to body-frame velocities: x, y, theta),
        and a camera frame. Receives over ZMQ, translate to body-frame vel
        """
        if not self.is_connected:
            raise DeviceNotConnectedError("URClient is not connected. You need to run `robot.connect()`.")

        obs_dict = {}
        if use_camera:
            # assert len(self.cameras) == 1, f"URClient should have exactly one camera configured, change the config_ur.py if needed. But {len(self.cameras)}"
            for keys, cam_dict in self.cameras.items():
                obs_dict[keys] = cam_dict.read()
            
        robot_pose = self.robot.get_observations().copy()

        obs_dict["ee_pos_rot"] = robot_pose["ee_pos_rot"]
        obs_dict["joint_positions"] = robot_pose["joint_positions"]
        obs_dict["joint_velocities"] = robot_pose["joint_velocities"]

        for i in range(len(robot_pose["ee_pos_rot"])):
            obs_dict[f"ee_pos_rot_{i}"] = robot_pose["ee_pos_rot"][i]
            
        for i in range(len(robot_pose["joint_positions"])):
            obs_dict[f"joint_positions_{i}"] = robot_pose["joint_positions"][i]
            
        for i in range(len(robot_pose["joint_velocities"])):
            obs_dict[f"joint_velocities_{i}"] = robot_pose["joint_velocities"][i]

        return obs_dict

    def configure(self):
        pass

    def send_action(self, action, method='joint', wait=False) -> dict[str, Any]:
        # method = 'joint'
        # for k in action.keys():
        #     if 'ee_pos_rot' in k:
        #         method = 'tcp'
        #         break
        if method == 'ee':
            action = np.array([action[f'ee_pos_rot_{i}'] for i in range(self.robot.num_tcp_dofs())])  # repeat for each arm
            self.step_tcp(action, wait=wait)
        # elif method == 'tcp_delta':
        #     robot_pose = self.robot.get_observations().copy()
        #     action= np.concatenate((action[:3] + robot_pose["ee_pos_rot"][:3], action[3:6] + robot_pose["ee_pos_rot"][3:6], action[6:7]))
        #     self.step_tcp(action, wait=wait)
        else:
            action = np.array([action[f'joint_positions_{i}'] for i in range(self.robot.num_dofs())])  # repeat for each arm
            self.step_joint(action, wait=wait)
        
        return self.get_observation()
    
    def step_joint(self, action: np.ndarray, wait=True) -> dict[str, Any]:
        self.robot.command_joint_state(action)
        
    def step_tcp(self, action: np.ndarray, wait=True) -> dict[str, Any]:
        self.robot.command_tcp_state(action)
        
    def disconnect(self):
        pass
        

class UR30Bimanual(UR30):
    config_class = UR30BimanualConfig
    name = "ur30_bimanual"

    def __init__(self, config: UR30BimanualConfig):
        super().__init__(config)
        self.num_dofs = 14
        self.num_tcp_dofs = 14
        