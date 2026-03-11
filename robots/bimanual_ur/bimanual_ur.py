import logging
from typing import Any

import numpy as np

from .config import BimanualURConfig, URConfig
from .ur import UR
from .realsense_camera import RealSenseCamera

logger = logging.getLogger(__name__)


class BimanualUR:
    """Bimanual UR robot wrapping two UR arm instances + cameras."""

    def __init__(self, config: BimanualURConfig):
        self.config = config
        self.num_dofs = 14
        self.num_tcp_dofs = 14

        left_config = URConfig(
            robot_ip=config.left_robot_ip,
            use_gripper=config.use_gripper,
            gripper_port=config.left_gripper_port,
            gripper_threshold=config.gripper_threshold,
            binarize_gripper=config.binarize_gripper,
            gripper_limits=config.gripper_limits,
            init_joint_positions=config.left_init_joint_positions,
            init=False,
        )
        right_config = URConfig(
            robot_ip=config.right_robot_ip,
            use_gripper=config.use_gripper,
            gripper_port=config.right_gripper_port,
            gripper_threshold=config.gripper_threshold,
            binarize_gripper=config.binarize_gripper,
            gripper_limits=config.gripper_limits,
            init_joint_positions=config.right_init_joint_positions,
            init=False,
        )

        self.left_arm = UR(left_config)
        self.right_arm = UR(right_config)

        # Create cameras
        self.cameras = {}
        for name, serial in config.camera_serial_numbers.items():
            self.cameras[name] = RealSenseCamera(
                serial_number=serial,
                width=config.camera_width,
                height=config.camera_height,
                fps=config.camera_fps,
            )

        if config.init:
            print("Go to home pose")
            self.go_home()

    def connect(self):
        for cam in self.cameras.values():
            cam.connect()

    def go_home(self):
        self.left_arm.rest_home_pose()
        self.right_arm.rest_home_pose()

    def get_observation(self, use_camera=True) -> dict[str, Any]:
        obs_dict = {}
        if use_camera:
            for key, cam in self.cameras.items():
                obs_dict[key] = cam.read()

        left_tcp = self.left_arm.get_tcp_state()
        right_tcp = self.right_arm.get_tcp_state()
        left_joints = self.left_arm.get_joint_state()
        right_joints = self.right_arm.get_joint_state()

        obs_dict["ee_pos_rot"] = np.concatenate([left_tcp, right_tcp])
        obs_dict["joint_positions"] = np.concatenate([left_joints, right_joints])

        return obs_dict

    def send_action(self, action: dict, action_type: str = "joint") -> None:
        if action_type in ("joint", "gello"):
            joint_action = np.array([action[f"joint_positions_{i}"] for i in range(self.num_dofs)])
            self.left_arm.step_joint(joint_action[:7])
            self.right_arm.step_joint(joint_action[7:])
        elif action_type == "tcp":
            tcp_action = np.array([action[f"ee_pos_rot_{i}"] for i in range(self.num_tcp_dofs)])
            self.left_arm.step_tcp(tcp_action[:7])
            self.right_arm.step_tcp(tcp_action[7:])
        else:
            raise ValueError(f"Unknown action_type: {action_type}")

    def disconnect(self):
        self.left_arm.disconnect()
        self.right_arm.disconnect()
        for cam in self.cameras.values():
            cam.disconnect()
