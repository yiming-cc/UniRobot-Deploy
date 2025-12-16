from lerobot.robots.robot import Robot
from .config_robot import RobotTemplateConfig
from typing import Any



class RobotTemplate(Robot):
    config_class = RobotTemplateConfig
    name = "robot"

    def __init__(self, config: RobotTemplateConfig):
        super().__init__(config)
        pass
    
    def get_observation(self) -> dict[str, Any]:
        pass

    def send_action(self, action: dict[str, Any]) -> dict[str, Any]:
        pass
    
    @property
    def observation_features(self) -> dict:
        pass

    @property
    def action_features(self) -> dict:
        pass

    @property
    def is_connected(self) -> bool:
        pass

    def connect(self, calibrate: bool = True) -> None:
        pass

    @property
    def is_calibrated(self) -> bool:
        pass

    def calibrate(self) -> None:
        pass

    def configure(self) -> None:
        pass

    def disconnect(self) -> None:
        pass