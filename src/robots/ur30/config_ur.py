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

from lerobot.cameras.configs import CameraConfig, Cv2Rotation
from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.cameras.realsense.configuration_realsense import RealSenseCameraConfig
from lerobot.cameras.configs import ColorMode
import numpy as np

from ..config import RobotConfig


@RobotConfig.register_subclass("ur30")
@dataclass
class UR30Config(RobotConfig):
    camera_type: str = "opencv"
    cameras: dict[str, CameraConfig] = field(
        default_factory=lambda: {
            # "left_wrist": OpenCVCameraConfig(
            #     index_or_path="/dev/video8",
            #     width=640,
            #     height=480,
            #     fps=30, 
            #     color_mode=ColorMode.RGB,
            # ),
            "front": OpenCVCameraConfig(
                index_or_path="/dev/video8",
                width=640,
                height=480,
                fps=30, 
                color_mode=ColorMode.RGB,
            ),
        }
    )
    
    zmq_port: int = 6001
    
    init: bool = True  # Whether to move the robot to the initial position on connect
    init_method: str = "joint"
    init_tcp_positions: list[float] = field(
        default_factory=lambda: [0.78739224, 0.18385742, 0.51242186, 2.19365512, 2.19028943, 0.07156651]
    )

    init_joint_positions: list[float] = field(
        default_factory=lambda: np.deg2rad(
                        [180, -90, 90, -90, -90, 0, 0],
                        # [180, -90, 90, -90, -90, -90, 0],
                        
                        
                        # [180, -60, 90, -90, -90, -90, 0],
                        # [180, -90, 90, 0, 90, 180, 0],
                        # [0, -90, -90, -90, 90, 180, 0]
                    ).tolist()
    )



@RobotConfig.register_subclass("ur30_bimanual")
@dataclass
class UR30BimanualConfig(RobotConfig):
    camera_type: str = "opencv"
    cameras: dict[str, CameraConfig] = field(
        default_factory=lambda: {
            "front": OpenCVCameraConfig(
                index_or_path="/dev/video4",
                width=640,
                height=480,
                fps=30, 
                color_mode=ColorMode.RGB,
            ),
        }
    )
    
    zmq_port: int = 6001
    
    init: bool = True  # Whether to move the robot to the initial position on connect
    init_method: str = "joint"
    # init_tcp_positions: list[float] = field(
    #     default_factory=lambda: [0.78739224, 0.18385742, 0.51242186, 2.19365512, 2.19028943, 0.07156651]
    # )
    init_joint_positions: list[float] = field(
        default_factory=lambda: np.deg2rad([
            180, -90, 90, -90, -90, 180, 0,
            0, -90, -90, -90, 90, 180, 0
            ]).tolist()
    )
