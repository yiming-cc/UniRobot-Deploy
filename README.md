# UniRobot-Deploy

双臂 UR 机器人的轻量级部署框架，用于 StarVLA 模型推理。

## 项目结构

```
UniRobot-Deploy/
├── inference.py                        # 主入口 — 最小控制循环
├── robots/
│   └── bimanual_ur/
│       ├── config.py                   # BimanualURConfig / URConfig 数据类
│       ├── bimanual_ur.py              # BimanualUR：封装双臂 + 相机
│       ├── ur.py                       # 单臂 UR 控制（RTDE + 夹爪）
│       ├── robotiq.py                  # Robotiq 2F-85 夹爪串口控制
│       ├── realsense_camera.py         # RealSense 相机封装
│       └── clients/
│           └── starvla_client.py       # StarVLA WebSocket 客户端 + 动作队列
├── utils/
│   └── msgpack_numpy.py               # 支持 numpy 数组的 msgpack 序列化
└── requirements.txt
```

## 环境搭建

### 1. 创建 conda 环境

```bash
conda create -n unirobot python=3.10 -y
conda activate unirobot
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

> **注意**：`ur-rtde` 依赖 UR RTDE C++ 库，Ubuntu 下安装方式：
> ```bash
> sudo add-apt-repository ppa:sdurobotics/ur-rtde
> sudo apt-get update
> sudo apt-get install librtde librtde-dev
> ```

### 3. 硬件连接

- 两台 UR 机械臂通过以太网连接（默认 IP：`192.168.1.100`、`192.168.2.100`）
- 两个 Robotiq 2F-85 夹爪通过 USB 串口连接（`/dev/ttyUSB0`、`/dev/ttyUSB1`）
- 三个 Intel RealSense 相机（顶部、左腕、右腕）

## 使用方法

### 运行推理

```bash
conda activate unirobot

python inference.py \
  --host="https://ai-notebook-inspire.sii.edu.cn/ws-9dcc0e1f-80a4-4af2-bc2f-0e352e7b17e6/project-97ab58cb-3162-4d0e-9137-1299d6cdea25/user-6d664c70-4a65-47de-8033-c7f0bd1610c6/vscode/8ba7e934-e894-4b31-ad5b-d00e4b4854ae/428e3bed-9e03-4144-b209-3bf6195b5401/proxy/10093/" \
  --task="Put all the items on the table into the drawer." \
  --action_type=joint \
  --fps=30 \
  --execution_steps=16 \
  --prefix_steps=8 \
  --rtc \
  --verbose
```

### 参数说明

| 参数 | 默认值 | 说明 |
|---|---|---|
| `--host` | （必填） | StarVLA 服务器 URL |
| `--port` | 无 | 服务器端口（如未包含在 URL 中） |
| `--task` | （必填） | VLA 模型的任务描述 |
| `--action_type` | `joint` | 控制模式：`joint`（关节空间）或 `tcp`（笛卡尔空间） |
| `--fps` | `30` | 控制循环频率 |
| `--execution_steps` | `16` | 每次推理执行的动作步数 |
| `--prefix_steps` | `8` | RTC 模式下的动作前缀步数 |
| `--rtc` / `--no-rtc` | `--rtc` | 启用/禁用实时控制异步模式 |
| `--verbose` | 关闭 | 打印时序信息 |
| `--debug` | 关闭 | 模拟机器人硬件（仅测试服务器连接） |

### 无硬件调试

```bash
python inference.py \
  --host="<StarVLA 服务器地址>" \
  --task="Put bottle" \
  --debug
```

## 硬件配置

机器人硬件参数定义在 `robots/bimanual_ur/config.py` 中，修改 `BimanualURConfig` 的默认值以匹配你的设备：

```python
@dataclass
class BimanualURConfig:
    left_robot_ip: str = "192.168.1.100"
    right_robot_ip: str = "192.168.2.100"
    left_gripper_port: str = "/dev/ttyUSB0"
    right_gripper_port: str = "/dev/ttyUSB1"
    camera_serial_numbers: dict = field(default_factory=lambda: {
        "top": "351322303100",
        "wrist_l": "352122274225",
        "wrist_r": "352122273073",
    })
    # ...
```

## 控制流程

```
Robot.get_observation()
    → 图像（3 路 RGB）+ 状态（14 维 TCP + 14 维关节角）
        → StarVLAClient.step()
            → 编码图像为 JPEG
            → 通过 WebSocket 发送（msgpack 序列化）
            → 接收服务器返回的 28 维动作
        → Robot.send_action()
            → 拆分为左/右臂动作
            → 通过 RTDE servoJ / servoL 执行
```

## RTC 模式

启用 `--rtc` 后，模型推理在后台线程中运行，动作队列持续填充，控制循环不会因等待服务器响应而阻塞。即使推理延迟超过控制周期，机器人仍能以目标帧率平滑运动。
