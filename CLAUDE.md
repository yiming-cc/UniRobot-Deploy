# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

UniRobot-Deploy 是一个基于 LeRobot 的统一机器人部署框架，允许将任意策略模型部署到任意机器人上。通过实现标准化接口，可以快速集成新的策略模型和机器人平台。

## 核心架构

项目采用三层架构：

1. **Policy Model Server**（远程）：运行在启智平台，接收观测数据（obs）和机器人状态（state），返回推理的动作（action chunk）
2. **Policy Client**（本地 `src/policies/`）：作为中转站，负责数据格式化
   - 接收 Robot 的原始数据，格式化后发送给 Server
   - 接收 Server 的动作预测，格式化后发送给 Robot
3. **Robot**（本地 `src/robots/`）：与机器人本体交互
   - 通过 SDK 获取机器人状态（关节位置、末端执行器姿态等）
   - 通过 SDK 控制机器人执行动作
   - 获取相机图像

数据流: Robot → Policy Client → Server → Policy Client → Robot

## 常用命令

### 运行部署
```bash
bash run.sh
```
主要执行 `lerobot_record.py`，配置 robot 类型、policy 类型、server URL 等参数。

### 环境设置
```bash
bash setup.sh
```
加载 G1 机器人的 SDK 环境变量（source a2d_sdk/env.sh）。

### 清理缓存
```bash
bash clean.sh
```
删除 LeRobot 数据集缓存目录。

### 主程序参数示例
```bash
python lerobot_record.py \
    --robot.type G1 \
    --dataset.repo_id ymc/eval_g1 \
    --dataset.single_task "任务描述" \
    --dataset.push_to_hub False \
    --dataset.episode_time_s 10000000 \
    --policy.type xvla_client \
    --policy.url <启智平台转发的URL>
```

## 代码结构

### src/policies/
Policy Client 实现，每个 policy 包含三个文件：
- `configuration_<policy>.py`: 配置类，继承自 `PreTrainedConfig`
- `modeling_<policy>.py`: 核心逻辑，继承自 `PreTrainedPolicy`，实现 `select_action()` 方法
- `processor_<policy>.py`: 数据处理器，负责格式化请求和响应

**关键方法**:
- `select_action(batch)`: 接收观测数据，返回动作（可能从缓存的 action chunk 中选择）
- `forward_process(batch)`: 将 Robot 数据格式化为 Server 需要的格式
- `backward_process(action_chunk)`: 将 Server 返回的动作格式化为 Robot 需要的格式

**已实现的 Policy**:
- `xvla_client`: X-VLA 模型客户端
- `go1_client`: GO1 模型客户端
- `openpi`: OpenPI 模型客户端
- `template`: 最小实现模板

### src/robots/
Robot 实现，每个 robot 包含两个文件：
- `config_<robot>.py`: 配置类，继承自 `RobotConfig`
- `<robot>.py`: 核心逻辑，继承自 `Robot`

**必须实现的方法**:
- `get_observation()`: 返回包含状态和图像的观测字典
- `send_action(action)`: 接收动作字典，控制机器人执行
- `observation_features`: 属性，定义观测空间的特征（形状、类型等）
- `action_features`: 属性，定义动作空间的特征
- `connect()`, `disconnect()`, `calibrate()`: 连接管理

**已实现的 Robot**:
- `g1`: 智元 G1 人形机器人（使用 a2d_sdk）
- `ur30`: UR30 机械臂
- `template`: 最小实现模板

### src/utils/
工具函数：
- `rotation_utils.py`: 旋转表示转换（欧拉角、四元数、旋转矩阵等）
- `img_utils.py`: 图像处理（resize、center crop 等）
- `visualize_utils.py`: 可视化工具（action chunk 可视化等）
- `import_utils.py`: 动态导入工具

### 主程序
- `lerobot_record.py`: 从 LeRobot 框架修改而来，协调 Policy 和 Robot，处理数据采集流程

## 添加新的 Policy 或 Robot

### 添加新 Policy
1. 在 `src/policies/` 创建新目录
2. 参考 `template` 实现三个文件
3. 实现 `select_action()` 方法，通常通过 HTTP 请求与远程 server 通信
4. 实现数据格式化逻辑（forward_process 和 backward_process）

### 添加新 Robot
1. 在 `src/robots/` 创建新目录
2. 参考 `template` 实现配置和主类
3. 实现 `get_observation()` 和 `send_action()` 方法
4. 定义 `observation_features` 和 `action_features`
5. 实现连接、校准等管理方法

## 重要概念

### Action Chunk
策略模型通常一次推理返回多个时间步的动作序列（action chunk），而不是单步动作。Policy Client 会缓存这些动作，每次调用 `select_action()` 时从缓存中取出一个动作，直到缓存用完再请求新的 chunk。

### 数据格式
- **观测（Observation）**: 包含图像（字典键如 "head", "hand_left" 等）和状态（"observation.state" 张量）
- **动作（Action）**: 包含末端执行器姿态、关节角度、夹爪状态等，具体格式取决于 robot 实现

### G1 机器人特殊说明
- 使用 `a2d_sdk` 进行通信（RobotDds, RobotController, CosineCamera）
- 支持双臂控制和三个相机（头部、左手、右手）
- 需要先运行 `setup.sh` 加载 SDK 环境

## 依赖项

### 必需依赖
- **LeRobot**: 必须从源码安装 (`pip install -e .`)
  ```bash
  git clone git@github.com:huggingface/lerobot.git
  cd lerobot && pip install -e .
  ```
- **json_numpy**: 用于 JSON 序列化包含 numpy 数组的数据

### Robot 特定依赖
- G1: `a2d_sdk`（在 `src/robots/g1/a2d_sdk/` 中提供）
- G1 GUI（可选）: 见 `src/robots/g1/requirements_gui.txt`

## 开发注意事项

- 所有 Policy 和 Robot 类必须有 `name` 类属性和 `config_class` 类属性
- Policy 的 `select_action()` 方法必须返回形状正确的 Tensor
- Robot 的 `observation_features` 和 `action_features` 必须与实际数据格式匹配
- 图像数据通常需要 resize 和 center crop 到统一尺寸（如 480x640）
- G1 机器人的动作可以是末端执行器姿态（is_eef=True）或关节角度（is_eef=False）
