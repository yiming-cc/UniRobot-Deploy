# UR5e 机器人集成

这个目录包含了 UR5e 机械臂的集成实现，使用 RTDE（Real-Time Data Exchange）协议直接控制机器人。

## 文件说明

- `config_ur5e.py`: UR5e 配置类，定义机器人参数
- `ur5e.py`: UR5e 主实现类，包含控制逻辑
- `robotiq.py`: Robotiq 夹爪驱动（Modbus RTU 通信）
- `__init__.py`: 包初始化文件

## 硬件要求

1. **UR5e 机械臂**: 通过以太网连接（默认 IP: 192.168.1.100）
2. **Robotiq 夹爪**: 通过 USB 转串口连接（默认 /dev/ttyUSB1）
3. **RealSense 相机**: 两个 D405 深度相机（顶部和手腕）

## 依赖项安装

```bash
# 安装 UR RTDE 库
pip install ur_rtde

# 安装串口通信库
pip install pyserial

# RealSense 库已通过 lerobot 安装
```

## 硬件配置

### 1. 发现摄像头序列号

```bash
rs-enumerate-devices | grep "Serial Number"
```

将序列号更新到 `config_ur5e.py` 的 `cameras` 配置中。

### 2. 测试夹爪连接

```python
from src.robots.ur5e.robotiq import CtrlGrp
gripper = CtrlGrp("/dev/ttyUSB1")
gripper.ACT()  # 应该成功激活
```

如果遇到权限问题：
```bash
sudo usermod -aG dialout $USER
# 然后注销并重新登录
```

### 3. 测试 RTDE 连接

```python
import rtde_receive
r = rtde_receive.RTDEReceiveInterface("192.168.1.100")
print(r.getActualQ())  # 应该返回 6 个关节角度
```

## 使用方法

### 基本使用

```bash
bash run_ur5e.sh
```

### 自定义参数

```bash
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
```

## 配置说明

### 控制方法

- `control_method="joint"`: 关节空间控制（推荐，更稳定）
- `control_method="tcp"`: TCP 空间控制（可能在奇异点附近不稳定）

### 初始化方法

- `init_method="joint"`: 使用关节角度初始化
- `init_method="tcp"`: 使用 TCP 姿态初始化

### 夹爪配置

- `binarize_gripper=False`: 连续夹爪控制（0-1）
- `binarize_gripper=True`: 二值化夹爪控制（完全打开/完全关闭）
- `gripper_threshold=0.5`: 二值化阈值

## 观测空间

- **关节状态** (`joint_positions_0` 到 `joint_positions_6`): 6 个关节角度 + 1 个夹爪位置
- **TCP 状态** (`ee_pos_rot_0` 到 `ee_pos_rot_6`): xyz + rotvec + 夹爪位置
- **摄像头图像** (`top`, `wrist`): 480x270 RGB 图像

## 动作空间

- **关节动作** (`joint_positions_0` 到 `joint_positions_6`): 目标关节角度 + 夹爪位置
- **TCP 动作** (`ee_pos_rot_0` 到 `ee_pos_rot_6`): 目标 TCP 姿态 + 夹爪位置

## 安全特性

- **关节增量限制**: 单次移动不超过 0.5 rad
- **角度环绕处理**: 自动处理 -π 到 π 的角度跳变
- **夹爪异步控制**: 120 Hz 独立线程，避免阻塞主循环

## 故障排查

### RTDE 连接失败

1. 检查网络连接: `ping 192.168.1.100`
2. 确认 UR 机器人未被其他程序占用
3. 在 UR 示教器上启用 RTDE 接口

### 夹爪无响应

1. 检查串口权限: `ls -l /dev/ttyUSB1`
2. 检查串口设备: `dmesg | grep ttyUSB`
3. 检查 Robotiq 夹爪电源

### 摄像头无法识别

1. 列出所有 RealSense 设备: `rs-enumerate-devices`
2. 检查 USB 3.0 连接: `lsusb | grep Intel`
3. 确保使用 USB 3.0 端口（蓝色）

### 关节增量超限

- 检查策略模型是否正确训练
- 降低动作预测的缩放因子
- 调整 `max_joint_delta` 阈值（谨慎）

## 性能指标

- **控制频率**: 20-30 Hz
- **观测获取**: < 5 ms
- **动作执行**: < 2 ms（关节控制）
- **夹爪响应**: 120 Hz 独立线程

## 参考

- [UR RTDE 文档](https://sdurobotics.gitlab.io/ur_rtde/)
- [Robotiq 夹爪文档](https://robotiq.com/support)
- [RealSense SDK](https://github.com/IntelRealSense/librealsense)
