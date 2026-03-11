from dataclasses import dataclass, field
import numpy as np


@dataclass
class URConfig:
    robot_ip: str = "192.168.1.100"
    use_gripper: bool = True
    gripper_port: str = "/dev/ttyUSB0"
    gripper_threshold: float = 0.5
    binarize_gripper: bool = False
    gripper_limits: list = field(default_factory=lambda: [0.01, 0.90])
    init_joint_positions: list = field(
        default_factory=lambda: np.deg2rad([90, -90, 90, -90, -90, -180, 0]).tolist()
    )
    init: bool = True


@dataclass
class BimanualURConfig:
    left_robot_ip: str = "192.168.1.100"
    right_robot_ip: str = "192.168.2.100"

    use_gripper: bool = True
    left_gripper_port: str = "/dev/ttyUSB0"
    right_gripper_port: str = "/dev/ttyUSB1"
    gripper_threshold: float = 0.5
    binarize_gripper: bool = False
    gripper_limits: list = field(default_factory=lambda: [0.01, 0.90])

    camera_serial_numbers: dict = field(
        default_factory=lambda: {
            "top": "351322303100",
            "wrist_l": "352122274225",
            "wrist_r": "352122273073",
        }
    )
    camera_width: int = 640
    camera_height: int = 480
    camera_fps: int = 30

    init: bool = True

    left_init_joint_positions: list = field(
        default_factory=lambda: np.deg2rad([90, -90, 90, -90, -90, -180, 0]).tolist()
    )
    right_init_joint_positions: list = field(
        default_factory=lambda: np.deg2rad([-90, -90, -90, -90, 90, 0, 0]).tolist()
    )
