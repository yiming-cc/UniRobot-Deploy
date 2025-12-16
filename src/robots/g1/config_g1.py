from lerobot.robots.config import RobotConfig
from dataclasses import dataclass, field
from lerobot.cameras import CameraConfig



@RobotConfig.register_subclass("G1")
@dataclass
class G1Config(RobotConfig):
    # cameras: dict[str, CameraConfig] = field(default_factory=dict)

    canonical_pose_file: str = "res/canonical_pose.json"
