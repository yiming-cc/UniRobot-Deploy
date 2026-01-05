from a2d_sdk.robot import RobotDds as Robot
from a2d_sdk.robot import RobotController
from a2d_sdk.robot import CosineCamera as Camera
import time
import sys
import json
from PIL import Image
from cv2 import line
import numpy as np


def resize_center_crop(img, target_h: int, target_w: int):
    """
    将图像按比例缩放后进行中心裁剪到指定尺寸 (target_h, target_w)，保证不拉伸、不形变。

    参数:
        img: 输入图像，可以是 numpy.ndarray (H, W, C) 或 PIL.Image.Image
        target_h: 目标高度
        target_w: 目标宽度

    返回:
        numpy.ndarray，形状为 (target_h, target_w, C)
    """
    # 转成 PIL Image 统一处理
    if isinstance(img, np.ndarray):
        pil_img = Image.fromarray(img)
    else:
        pil_img = img

    w, h = pil_img.size

    # 先按长边缩放，使得缩放后图像可以覆盖目标尺寸，再中心裁剪
    scale = max(target_w / w, target_h / h)
    new_w = int(round(w * scale))
    new_h = int(round(h * scale))

    pil_img = pil_img.resize((new_w, new_h), Image.BILINEAR)

    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    right = left + target_w
    bottom = top + target_h

    pil_img = pil_img.crop((left, top, right, bottom))

    return np.array(pil_img)


if __name__ == "__main__":
    # --------------------- robot basic control --------------------- # 
    # robot = Robot()
    # time.sleep(0.5) #等待资源初始化，收到消息

    # arm_joint_states = robot.arm_joint_states()
    # print(arm_joint_states)

    # gripper_states = robot.gripper_states()
    # print(gripper_states)

    # body_pose_joint_states = robot.body_pose_joint_states()
    # print(body_pose_joint_states)

    # robot.move_head([0.0, 0.0]) # 控制头部运动
    # print("move head done")
    # robot.move_gripper([120, 35]) # 控制夹持器
    # print("move gripper done")
    # robot.shutdown()
    # print("shutdown done")

    # motion_status = robot.get_motion_status()
    # print(motion_status)

    # whole_body_status = robot.whole_body_status()
    # print(whole_body_status)

    # body_pose_joint_states = robot.body_pose_joint_states()
    # print(body_pose_joint_states)

    # --------------------- robot basic control --------------------- # 

    # --------------------- robot end effector pose control --------------------- # 

    # with open("canonical_pose.json", "r") as f:
    #     canonical_pose = json.load(f)
    
    # robot_controller = RobotController()
    # time.sleep(0.5) #等待资源初始化，收到消息

    # motion_status = robot_controller.get_motion_status()
    


    # with open("motion_status.json", "w") as f:
    #     json.dump(motion_status, f)
    
    # left_pose = motion_status["frames"]["arm_left_link7"]["position"]
    # left_pose["qx"] = motion_status["frames"]["arm_left_link7"]["orientation"]["quaternion"]["x"]
    # left_pose["qy"] = motion_status["frames"]["arm_left_link7"]["orientation"]["quaternion"]["y"]
    # left_pose["qz"] = motion_status["frames"]["arm_left_link7"]["orientation"]["quaternion"]["z"]
    # left_pose["qw"] = motion_status["frames"]["arm_left_link7"]["orientation"]["quaternion"]["w"]
    
    # left_pose["y"] += 0.1

    # right_pose = motion_status["frames"]["arm_right_link7"]["position"]
    # right_pose["qx"] = motion_status["frames"]["arm_right_link7"]["orientation"]["quaternion"]["x"]
    # right_pose["qy"] = motion_status["frames"]["arm_right_link7"]["orientation"]["quaternion"]["y"]
    # right_pose["qz"] = motion_status["frames"]["arm_right_link7"]["orientation"]["quaternion"]["z"]
    # right_pose["qw"] = motion_status["frames"]["arm_right_link7"]["orientation"]["quaternion"]["w"]

    # right_pose["z"] += 0.05
    # right_pose["y"] += 0.1


    # robot_controller.set_end_effector_pose_control(2.0, ["left_arm", "right_arm"], left_pose=left_pose, right_pose=right_pose)
    
    # print(motion_status)
    # --------------------- robot end effector pose control --------------------- # 


    # --------------------- robot camera control --------------------- # 

    camera = Camera(["head", "hand_left", "hand_right"])
    time.sleep(0.5) #等待资源初始化，收到消息

    image, time_stamp = camera.get_latest_image("head")
    hand_left_image, _ = camera.get_latest_image("hand_left")
    hand_right_image, _ = camera.get_latest_image("hand_right")

    
    print(image.shape)
    print(hand_left_image.shape)
    print(hand_right_image.shape)

    image = resize_center_crop(image, 480, 640)
    hand_left_image = resize_center_crop(hand_left_image, 480, 640)
    hand_right_image = resize_center_crop(hand_right_image, 480, 640)

    Image.fromarray(image).save("res/camera_head.png")
    Image.fromarray(hand_left_image).save("res/camera_hand_left.png")
    Image.fromarray(hand_right_image).save("res/camera_hand_right.png")

    
    camera.close()
    print("camera closed")

    # --------------------- robot camera control --------------------- # 


    # --------------------- set canonical pose --------------------- # 

    # robot = Robot()
    # robot_controller = RobotController()
    # time.sleep(0.5) #等待资源初始化，收到消息

    # with open("/home/ymc/Project/UniRobot-Deploy/res/canonical_pose.json", "r") as f:
    #     canonical_pose = json.load(f)
    
    # robot.move_gripper(canonical_pose["observation.states.effector.position"])
    # robot.move_head(canonical_pose["observation.states.head.position"])

    # canonical_pose["observation.states.waist.position"][1] *= 100

    # # canonical_pose["observation.states.waist.position"][1] += 5

    # robot.reset(
    #     arm_positions=canonical_pose["observation.states.joint.position"],
    #     head_positions=canonical_pose["observation.states.head.position"],
    #     gripper_positions=canonical_pose["observation.states.effector.position"],
    #     waist_positions=canonical_pose["observation.states.waist.position"],
    # )

    # robot.move_wheel(linear=100.0, angular=0.0)


    # print(robot.arm_joint_states())

    # print("finish")
    
    # motion_status = robot_controller.get_motion_status()
    
    
    # with open("motion_status.json", "w") as f:
    #     json.dump(motion_status, f, indent=4)


    # time.sleep(1)
    # motion_status = robot_controller.get_motion_status()
    # with open("motion_status_2.json", "w") as f:
    #     json.dump(motion_status, f, indent=4)


    # robot.shutdown()


    # --------------------- set canonical pose --------------------- # 



    # sys.exit(0)