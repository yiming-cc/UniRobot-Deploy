from lerobot.robots.robot import Robot
from .config_g1 import G1Config
from typing import Any
from lerobot.cameras.utils import make_cameras_from_configs
from a2d_sdk.robot import RobotDds, RobotController, CosineCamera
import time
from PIL import Image
import json
from src.utils.img_utils import resize_center_crop

class G1(Robot):
    config_class = G1Config
    name = "G1"

    def __init__(self, config: G1Config):
        super().__init__(config)
        # self.cameras = make_cameras_from_configs(config.cameras)
        # len camera should be equal to len of camera_keys
        self.cameras = [None, None, None]


        self.camera_keys = ["head", "hand_left", "hand_right"]
        self.robot = None
        self.robot_controller = None
        self.robot_camera = None

        self.canonical_pose = json.load(open(config.canonical_pose_file)) if config.canonical_pose_file is not None else None
        self.canonical_pose["observation.states.waist.position"][1] *= 100 # m to cm
        
    def get_observation(self) -> dict[str, Any]:
        obs = {

        }

        motion_status = self.robot_controller.get_motion_status()
        
        obs["arm_left_x"] = motion_status["frames"]["arm_left_link7"]["xyzrpy"][0]
        obs["arm_left_y"] = motion_status["frames"]["arm_left_link7"]["xyzrpy"][1]
        obs["arm_left_z"] = motion_status["frames"]["arm_left_link7"]["xyzrpy"][2]
        obs["arm_left_roll"] = motion_status["frames"]["arm_left_link7"]["xyzrpy"][3]
        obs["arm_left_pitch"] = motion_status["frames"]["arm_left_link7"]["xyzrpy"][4]
        obs["arm_left_yaw"] = motion_status["frames"]["arm_left_link7"]["xyzrpy"][5]

        obs["arm_right_x"] = motion_status["frames"]["arm_right_link7"]["xyzrpy"][0]
        obs["arm_right_y"] = motion_status["frames"]["arm_right_link7"]["xyzrpy"][1]
        obs["arm_right_z"] = motion_status["frames"]["arm_right_link7"]["xyzrpy"][2]
        obs["arm_right_roll"] = motion_status["frames"]["arm_right_link7"]["xyzrpy"][3]
        obs["arm_right_pitch"] = motion_status["frames"]["arm_right_link7"]["xyzrpy"][4]
        obs["arm_right_yaw"] = motion_status["frames"]["arm_right_link7"]["xyzrpy"][5]


        gripper_states = self.robot.gripper_states()
        obs["gripper_left"] = gripper_states[0][0]
        obs["gripper_right"] = gripper_states[0][1]

        head, _ = self.robot_camera.get_latest_image("head")
        hand_left, _ = self.robot_camera.get_latest_image("hand_left")
        hand_right, _ = self.robot_camera.get_latest_image("hand_right")

        obs["head"] = resize_center_crop(head, 480, 640)
        obs["hand_left"] = resize_center_crop(hand_left, 480, 640)
        obs["hand_right"] = resize_center_crop(hand_right, 480, 640)

        # debug
        # Image.fromarray(head).save("res/camera_head.png")
        # Image.fromarray(hand_left).save("res/camera_hand_left.png")
        # Image.fromarray(hand_right).save("res/camera_hand_right.png")

        
        return obs

    def send_action(self, action: dict[str, Any]) -> dict[str, Any]:
        # print(action)
        left_pose = {
            "x": action["arm_left_x"],
            "y": action["arm_left_y"],
            "z": action["arm_left_z"],
            "qx": action["arm_left_qx"],
            "qy": action["arm_left_qy"],
            "qz": action["arm_left_qz"],
            "qw": action["arm_left_qw"],
        }
        right_pose = {
            "x": action["arm_right_x"],
            "y": action["arm_right_y"],
            "z": action["arm_right_z"],
            "qx": action["arm_right_qx"],
            "qy": action["arm_right_qy"],
            "qz": action["arm_right_qz"],
            "qw": action["arm_right_qw"],
        }
        self.robot_controller.set_end_effector_pose_control(2.0, ["left_arm", "right_arm"], left_pose, right_pose)
        self.robot.move_gripper([action["gripper_left"], action["gripper_right"]])


        # time.sleep(1)
    
    @property
    def observation_features(self) -> dict:
        return {
            # state
            "arm_left_x": float,
            "arm_left_y": float,
            "arm_left_z": float,
            "arm_left_roll": float,
            "arm_left_pitch": float,
            "arm_left_yaw": float,
            "gripper_left": float,

            "arm_right_x": float,
            "arm_right_y": float,
            "arm_right_z": float,
            "arm_right_roll": float,
            "arm_right_pitch": float,
            "arm_right_yaw": float,
            "gripper_right": float,
            
            # image
            "head": (480, 640, 3),
            "hand_left": (480, 640, 3),
            "hand_right": (480, 640, 3)
        }

    @property
    def action_features(self) -> dict:
        return {
            "arm_left_x": float,
            "arm_left_y": float,
            "arm_left_z": float,
            "arm_left_qx": float,
            "arm_left_qy": float,
            "arm_left_qz": float,
            "arm_left_qw": float,
            "gripper_left": float,

            "arm_right_x": float,
            "arm_right_y": float,
            "arm_right_z": float,
            "arm_right_qx": float,
            "arm_right_qy": float,
            "arm_right_qz": float,
            "arm_right_qw": float,
            "gripper_right": float,
        }

    @property
    def is_connected(self) -> bool:
        return self.robot is not None and self.robot_controller is not None and self.robot_camera is not None

    def connect(self, calibrate: bool = True) -> None:
        self.robot = RobotDds()
        self.robot_controller = RobotController()
        self.robot_camera = CosineCamera(self.camera_keys)
        time.sleep(0.5)

        # set initial pose
        if self.canonical_pose is not None:
            self.robot.reset(
                arm_positions=self.canonical_pose["observation.states.joint.position"],
                head_positions=self.canonical_pose["observation.states.head.position"],
                gripper_positions=self.canonical_pose["observation.states.effector.position"],
                waist_positions=self.canonical_pose["observation.states.waist.position"],
            )

    @property
    def is_calibrated(self) -> bool:
        pass

    def calibrate(self) -> None:
        pass

    def configure(self) -> None:
        pass

    def disconnect(self) -> None:
        pass