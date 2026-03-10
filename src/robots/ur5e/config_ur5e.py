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

from dataclasses import dataclass, field

import numpy as np
from lerobot.cameras.config import CameraConfig
from lerobot.cameras.realsense.configuration_realsense import RealSenseCameraConfig
from lerobot.robots.config import RobotConfig


@RobotConfig.register_subclass("ur5e")
@dataclass
class UR5eConfig(RobotConfig):
    """Configuration for UR5e robot with Robotiq gripper and RealSense cameras."""

    # RTDE connection
    robot_ip: str = "192.168.1.100"

    # Gripper configuration
    use_gripper: bool = True
    gripper_port: str = "/dev/ttyUSB1"
    gripper_threshold: float = 0.5
    binarize_gripper: bool = False
    gripper_limits: list[float] = field(
        default_factory=lambda: [0.01, 0.90]
    )  # min and max opening in meters

    # Control method: "joint" or "tcp"
    control_method: str = "joint"

    # Camera configuration (RealSense D405)
    cameras: dict[str, CameraConfig] = field(
        default_factory=lambda: {
            "top": RealSenseCameraConfig(
                serial_number_or_name="351322303100",  # Update with actual serial number
                width=480,
                height=270,
                fps=30,
            ),
            "wrist": RealSenseCameraConfig(
                serial_number_or_name="352122273073",  # Update with actual serial number
                width=480,
                height=270,
                fps=30,
            ),
        }
    )

    # Initialization configuration
    init: bool = True
    init_method: str = "joint"  # "joint" or "tcp"
    init_tcp_positions: list[float] = field(
        default_factory=lambda: [0.787, 0.184, 0.512, 2.194, 2.190, 0.072, 0.0]
    )
    init_joint_positions: list[float] = field(
        default_factory=lambda: np.deg2rad([90, -90, 90, -90, -90, -180, 0]).tolist()
    )
