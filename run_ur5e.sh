#!/bin/bash

# UR5e Robot Deployment Script
# This script runs the LeRobot recording pipeline with UR5e robot configuration

python lerobot_record.py \
    --robot.type ur5e \
    --robot.robot_ip 192.168.1.100 \
    --robot.use_gripper True \
    --robot.gripper_port /dev/ttyUSB1 \
    --robot.control_method joint \
    --robot.init True \
    --robot.init_method joint \
    --dataset.repo_id ${HF_USER}/ur5e_demo \
    --dataset.single_task "Pick and place demonstration" \
    --dataset.push_to_hub False \
    --dataset.episode_time_s 30 \
    --policy.type xvla_client \
    --policy.url <YOUR_POLICY_SERVER_URL>
