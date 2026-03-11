# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

UniRobot-Deploy 是双臂 UR 机器人的轻量级部署框架，用于 StarVLA 模型推理。通过 WebSocket 连接 StarVLA 推理服务器，实现视觉-语言-动作模型的实时控制。

## 常用命令

```bash
# 环境搭建
conda create -n unirobot python=3.10
conda activate unirobot
pip install -r requirements.txt
pip install -e /path/to/openpi/packages/openpi-client

# 运行推理（需连接硬件和 StarVLA 服务器）
python inference.py --host="ws://<server>:port/ws" --task="任务描述" --fps=30

# 无硬件调试模式（使用 MockStarVLAClient）
python inference.py --host="ws://<server>:port/ws" --task="test" --debug

# 关键参数
#   --action_type=joint|tcp    动作空间类型
#   --rtc / --no-rtc           是否启用异步推理（RTC 模式）
#   --execution_steps=16       每次推理执行的动作步数
#   --prefix_steps=8           RTC 模式下的前缀步数（平滑衔接）
#   --verbose / --debug        日志级别
```

无构建系统，纯 Python 项目。无测试套件。

## 架构

两层数据流：**推理循环** → **StarVLAClient（集成硬件控制 + 推理通信）**

```
inference.py (主控制循环, 30Hz)
  └── StarVLAClient (继承 WebsocketClientPolicy)
        ├── WebSocket 通信 (openpi-client, msgpack 序列化)
        ├── RTC 异步推理 (action queue + prefix 平滑控制)
        ├── UR × 2 (RTDE 控制, servoJ/servoL)
        │     └── Robotiq 2F-85 (Modbus RTU, 120Hz 后台线程)
        └── RealSenseCamera × 3 (top, wrist_l, wrist_r)
```

### 核心模块

- `inference.py` — 入口，argparse 参数解析 + 主循环，调用 `client.step()` 完成单帧
- `robots/bimanual_ur/clients/starvla_client.py` — StarVLA 客户端，集成硬件控制 + WebSocket 推理 + RTC 异步模式
- `robots/bimanual_ur/ur.py` — 单臂 RTDE 控制 + Robotiq 夹爪集成
- `robots/bimanual_ur/config.py` — 硬件配置 dataclass（IP、端口、相机序列号、初始关节角）

### 关键设计

- **Client 集成硬件**：StarVLAClient 继承 openpi-client 的 WebsocketClientPolicy，同时管理双臂和相机，`step()` 方法一次完成观测→推理→执行
- **RTC 模式**：推理和控制解耦，推理线程持续运行，控制循环从 action queue 消费动作，prefix steps 实现新旧动作序列平滑过渡
- **安全机制**：关节增量限制（0.8 rad），Home 位姿平滑插值
- **状态维度**：14 维（每臂 7D = TCP 位姿 + 夹爪），动作维度同理
- **通信协议**：图像 JPEG 编码 + msgpack 序列化（openpi_client.msgpack_numpy），经 WebSocket 传输

## 硬件默认配置

| 设备 | 地址 |
|------|------|
| 左臂 UR | 192.168.1.100 |
| 右臂 UR | 192.168.2.100 |
| 左夹爪 | /dev/ttyUSB0 |
| 右夹爪 | /dev/ttyUSB1 |

相机通过序列号区分（top, wrist_l, wrist_r），在 `config.py` 中配置。

## 扩展指南

添加新机器人+客户端：在 `robots/` 下创建新目录，客户端继承 `WebsocketClientPolicy` 并集成硬件控制，实现 `step()` 接口（观测→推理→执行），参考 `bimanual_ur/clients/starvla_client.py`。
