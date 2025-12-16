from lerobot.robots.config import RobotConfig
from dataclasses import dataclass, field
from lerobot.cameras import CameraConfig



@RobotConfig.register_subclass("robot_template")
@dataclass
class RobotTemplateConfig(RobotConfig):
    cameras: dict[str, CameraConfig] = field(default_factory=dict)
