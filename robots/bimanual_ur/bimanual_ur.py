import logging

from .config import BimanualURConfig, URConfig
from .ur import UR
from .realsense_camera import RealSenseCamera

logger = logging.getLogger(__name__)


class BimanualUR:
    """Bimanual UR robot: hardware init + lifecycle management.

    Exposes left_arm, right_arm, cameras for clients to use directly.
    """

    def __init__(self, config: BimanualURConfig = None):
        self.config = config or BimanualURConfig()
        cfg = self.config

        left_config = URConfig(
            robot_ip=cfg.left_robot_ip,
            use_gripper=cfg.use_gripper,
            gripper_port=cfg.left_gripper_port,
            gripper_threshold=cfg.gripper_threshold,
            binarize_gripper=cfg.binarize_gripper,
            gripper_limits=cfg.gripper_limits,
            init_joint_positions=cfg.left_init_joint_positions,
            init=False,
        )
        right_config = URConfig(
            robot_ip=cfg.right_robot_ip,
            use_gripper=cfg.use_gripper,
            gripper_port=cfg.right_gripper_port,
            gripper_threshold=cfg.gripper_threshold,
            binarize_gripper=cfg.binarize_gripper,
            gripper_limits=cfg.gripper_limits,
            init_joint_positions=cfg.right_init_joint_positions,
            init=False,
        )

        self.left_arm = UR(left_config)
        self.right_arm = UR(right_config)

        self.cameras = {}
        for name, serial in cfg.camera_serial_numbers.items():
            self.cameras[name] = RealSenseCamera(
                serial_number=serial,
                width=cfg.camera_width,
                height=cfg.camera_height,
                fps=cfg.camera_fps,
            )

        if cfg.init:
            logger.info("Go to home pose")
            self.go_home()

    def connect(self):
        for cam in self.cameras.values():
            cam.connect()

    def go_home(self):
        self.left_arm.rest_home_pose()
        self.right_arm.rest_home_pose()

    def disconnect(self):
        self.left_arm.disconnect()
        self.right_arm.disconnect()
        for cam in self.cameras.values():
            cam.disconnect()
