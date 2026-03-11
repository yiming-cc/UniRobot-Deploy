# UniRobot-Deploy

双臂 UR 机器人的轻量级部署框架，支持多种 VLA 模型推理客户端的即插即用切换。

## 项目结构

```
UniRobot-Deploy/
├── inference.py                        # 主入口 — 通用推理控制循环
├── run.sh                              # 快速启动脚本
├── robots/
│   ├── __init__.py                     # 客户端注册表 + 自动发现机制
│   └── bimanual_ur/                    # 双臂 UR 机器人
│       ├── config.py                   # BimanualURConfig / URConfig 数据类
│       ├── bimanual_ur.py              # BimanualUR：封装双臂 + 相机生命周期
│       ├── ur.py                       # 单臂 UR 控制（RTDE + 夹爪）
│       ├── robotiq.py                  # Robotiq 2F-85 夹爪串口控制
│       ├── realsense_camera.py         # RealSense 相机封装
│       └── clients/
│           ├── __init__.py             # 注册该机器人下的所有客户端（lazy import）
│           ├── starvla_client.py       # StarVLA WebSocket 客户端
│           └── dreamzero_client.py     # DreamZero 客户端（待实现）
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

---

## 使用方法

### 查看可用客户端与参数

```bash
# 查看所有已注册客户端
python inference.py --help

# 查看特定客户端的专属参数
python inference.py --client=bimanual_ur_starvla --help
python inference.py --client=bimanual_ur_dreamzero --help
```

### 运行推理

通过 `--client` 参数切换不同的推理客户端，命令行参数会根据所选客户端自动调整：

```bash
# 使用 StarVLA 客户端（默认）
python inference.py \
  --client=bimanual_ur_starvla \
  --host="ws://<server>:<port>/ws" \
  --task="Put all the items on the table into the drawer." \
  --action_type=joint \
  --fps=30 \
  --execution_steps=16 \
  --prefix_steps=8 \
  --rtc \
  --verbose

# 使用 DreamZero 客户端（切换只需改 --client）
python inference.py \
  --client=bimanual_ur_dreamzero \
  --host="ws://<server>:<port>/ws" \
  --task="Pick up the cup." \
  --action_type=joint \
  --fps=30 \
  --verbose
```

### 无硬件调试

```bash
python inference.py \
  --client=bimanual_ur_starvla \
  --host="ws://<server>:<port>/ws" \
  --task="test" \
  --debug
```

`--debug` 会跳过真实硬件和服务器连接，使用内置 MockClient 运行空循环，用于验证参数解析和控制循环逻辑。

### 通用参数

| 参数 | 默认值 | 说明 |
|---|---|---|
| `--client` | `bimanual_ur_starvla` | 选择推理客户端（从注册表自动发现） |
| `--host` | （必填） | 推理服务器 URL |
| `--port` | 无 | 服务器端口（如未包含在 URL 中） |
| `--task` | （必填） | VLA 模型的任务描述 |
| `--fps` | `30` | 控制循环频率 |
| `--verbose` | 关闭 | 打印时序信息 |
| `--debug` | 关闭 | 模拟模式，不连接硬件和服务器 |

### StarVLA 专属参数

以下参数仅在 `--client=bimanual_ur_starvla` 时可用：

| 参数 | 默认值 | 说明 |
|---|---|---|
| `--action_type` | `joint` | 控制模式：`joint`（关节空间）或 `tcp`（笛卡尔空间） |
| `--execution_steps` | `16` | 每次推理执行的动作步数 |
| `--prefix_steps` | `8` | RTC 模式下的动作前缀步数 |
| `--rtc` / `--no-rtc` | `--rtc` | 启用/禁用实时控制异步模式 |

---

## 架构设计

### 核心概念

框架采用 **机器人 (Robot)** 与 **客户端 (Client)** 分离的两层架构：

```
inference.py (通用控制循环)
    │
    │  --client=xxx 选择
    ▼
CLIENT_REGISTRY ──→ factory(args) ──→ (robot, client)
    │
    ▼
┌──────────────────────────────────────────────┐
│  Robot 层：硬件生命周期管理                      │
│  connect() / disconnect() / go_home()         │
│  暴露 arms, cameras 供 Client 层使用            │
├──────────────────────────────────────────────┤
│  Client 层：推理协议 + 动作执行                  │
│  step(task_description, fps) → action         │
│  内部完成：观测采集 → 推理通信 → 动作执行          │
└──────────────────────────────────────────────┘
```

- **Robot**：负责硬件初始化、连接、断开，向上暴露统一的传感器和执行器接口
- **Client**：负责与推理服务器通信，调用 Robot 接口完成"观测 → 推理 → 执行"闭环
- **inference.py**：不感知具体硬件和协议，只调用 `client.step()` + 控制循环节拍

### 客户端注册表

`robots/__init__.py` 中维护全局 `CLIENT_REGISTRY`，通过自动发现机制加载所有 `robots/*/clients/__init__.py`，触发各模块的 `register_client()` 调用：

```
robots/__init__.py                 # CLIENT_REGISTRY + auto-discover
    ↓ import
robots/bimanual_ur/clients/__init__.py    # register_client("bimanual_ur_starvla", ...)
                                          # register_client("bimanual_ur_dreamzero", ...)
    ↓ lazy import (仅在 factory 被调用时)
robots/bimanual_ur/clients/starvla_client.py      # StarVLAClient 实现
robots/bimanual_ur/clients/dreamzero_client.py    # DreamZeroClient 实现
```

注册表条目包含三个部分：

| 字段 | 类型 | 说明 |
|---|---|---|
| `description` | `str` | 客户端的简短描述 |
| `factory` | `(args) → (robot, client)` | 工厂函数：接收 argparse 命名空间，创建并返回 robot 和 client 实例 |
| `add_arguments` | `(parser) → None` | 可选，向 argparse 添加该客户端的专属命令行参数 |

### RTC 模式

启用 `--rtc` 后，推理在后台线程运行，动作队列持续填充，控制循环不会因等待推理响应而阻塞。`prefix_steps` 用于新旧动作序列的平滑衔接。

### 控制流程

```
client.step(task_description, fps)
    │
    ├─ 1. robot.get_observation()
    │     → 图像（N 路 RGB）+ 状态（TCP 位姿 + 关节角）
    │
    ├─ 2. 编码 → 发送推理请求 → 接收动作序列
    │     （sync 模式：阻塞等待；RTC 模式：后台线程异步推理）
    │
    └─ 3. robot.send_action()
          → 拆分为各臂动作 → RTDE servoJ/servoL 执行
```

---

## 扩展指南

### 场景一：为已有机器人添加新客户端

以在 `bimanual_ur` 上添加 `FooClient` 为例。

#### 第一步：创建客户端实现文件

```bash
# 新建文件
robots/bimanual_ur/clients/foo_client.py
```

```python
"""Foo inference client for bimanual UR."""

import logging
from typing import Optional
import numpy as np

logger = logging.getLogger(__name__)


class FooClient:
    """Foo 推理客户端。

    必须实现以下接口：
    - step(task_description, fps, ...) → np.ndarray  # 单帧推理+执行
    - close()                                         # 清理资源
    """

    def __init__(
        self,
        host: str,
        port: Optional[int] = None,
        robot=None,           # BimanualUR 实例，由 factory 注入
        fps: int = 30,
        action_type: str = "joint",
        verbose: bool = False,
        # ... 添加 Foo 协议特有的参数
    ):
        self.robot = robot
        self.host = host
        self.port = port
        self.fps = fps
        self.action_type = action_type
        self.verbose = verbose
        # TODO: 初始化与 Foo 推理服务器的连接

    def step(self, task_description=None, fps=None, action_type=None, view_mask=None):
        """单帧步骤：观测 → 推理 → 执行。"""
        # 1. 采集观测
        obs = self._get_observation()

        # 2. 发送推理请求、接收动作
        action = self._infer(obs, task_description)

        # 3. 执行动作
        self._send_action(action)

        return action

    def close(self):
        """断开与推理服务器的连接。"""
        pass

    # --- 内部方法 ---

    def _get_observation(self):
        """从 robot 获取观测数据。"""
        images = {k: cam.read() for k, cam in self.robot.cameras.items()}
        left_tcp = self.robot.left_arm.get_tcp_state()
        right_tcp = self.robot.right_arm.get_tcp_state()
        return {"images": images, "state": np.concatenate([left_tcp, right_tcp])}

    def _infer(self, obs, task_description):
        """向推理服务器发送请求并返回动作。"""
        raise NotImplementedError("TODO: 实现 Foo 推理协议")

    def _send_action(self, action):
        """将动作发送给机器人执行。"""
        joint_action = action[:14]  # 根据实际协议调整
        self.robot.left_arm.step_joint(joint_action[:7])
        self.robot.right_arm.step_joint(joint_action[7:])
```

#### 第二步：在 `clients/__init__.py` 中注册

```python
# robots/bimanual_ur/clients/__init__.py
# 在文件末尾追加：

# ── Foo ──────────────────────────────────────────────────────────

def _foo_add_arguments(parser):
    """添加 Foo 客户端专属的命令行参数。"""
    parser.add_argument("--action_type", type=str, default="joint", choices=["joint", "tcp"])
    parser.add_argument("--foo_param", type=int, default=42, help="Foo 特有参数")


def _foo_factory(args):
    """创建 BimanualUR + FooClient，仅在实际使用时才 import 重依赖。"""
    from .foo_client import FooClient
    from ..config import BimanualURConfig
    from ..bimanual_ur import BimanualUR

    config = BimanualURConfig()
    robot = BimanualUR(config)
    robot.connect()
    client = FooClient(
        host=args.host, port=args.port, robot=robot,
        fps=args.fps, action_type=args.action_type, verbose=args.verbose,
    )
    return robot, client


register_client("bimanual_ur_foo", "Bimanual UR + Foo", _foo_factory, _foo_add_arguments)
```

完成后即可使用：

```bash
python inference.py --client=bimanual_ur_foo --host="ws://..." --task="..." --foo_param=100
```

---

### 场景二：添加全新的机器人种类

以添加一个名为 `single_panda` 的 Franka Panda 单臂机器人为例。

#### 第一步：创建机器人目录结构

```bash
robots/
└── single_panda/
    ├── __init__.py
    ├── config.py
    ├── panda.py
    └── clients/
        ├── __init__.py           # 注册该机器人下的所有客户端
        └── starvla_client.py     # 或其他推理客户端
```

#### 第二步：定义配置

```python
# robots/single_panda/config.py
from dataclasses import dataclass, field

@dataclass
class PandaConfig:
    robot_ip: str = "192.168.1.50"
    use_gripper: bool = True
    camera_serial_numbers: dict = field(default_factory=lambda: {
        "top": "123456789",
        "wrist": "987654321",
    })
    camera_width: int = 640
    camera_height: int = 480
    camera_fps: int = 30
```

#### 第三步：实现机器人控制层

```python
# robots/single_panda/panda.py

class Panda:
    """Franka Panda 单臂机器人控制。

    必须实现以下接口供 Client 层使用：
    - connect()      # 建立硬件连接（相机等）
    - disconnect()    # 断开所有硬件连接
    """

    def __init__(self, config: PandaConfig):
        self.config = config
        # 初始化机械臂、相机等

    def connect(self):
        """连接相机等外设。"""
        pass

    def disconnect(self):
        """断开所有连接。"""
        pass
```

#### 第四步：实现客户端并注册

```python
# robots/single_panda/clients/__init__.py
from robots import register_client


def _starvla_add_arguments(parser):
    parser.add_argument("--action_type", type=str, default="joint", choices=["joint", "tcp"])
    parser.add_argument("--execution_steps", type=int, default=16)


def _starvla_factory(args):
    from .starvla_client import PandaStarVLAClient
    from ..config import PandaConfig
    from ..panda import Panda

    config = PandaConfig()
    robot = Panda(config)
    robot.connect()
    client = PandaStarVLAClient(
        host=args.host, port=args.port, robot=robot,
        fps=args.fps, action_type=args.action_type, verbose=args.verbose,
        execution_steps=args.execution_steps,
    )
    return robot, client


register_client("single_panda_starvla", "Franka Panda + StarVLA", _starvla_factory, _starvla_add_arguments)
```

```python
# robots/single_panda/__init__.py
from .config import PandaConfig
from .panda import Panda
```

完成后，`robots/__init__.py` 的自动发现会在导入时扫描到 `robots/single_panda/clients/__init__.py`，自动注册该客户端。无需修改 `inference.py` 或 `robots/__init__.py`。

```bash
# 直接可用
python inference.py --client=single_panda_starvla --host="ws://..." --task="..."
```

---

## 关键约定

### 客户端接口规范

所有客户端必须实现以下方法，才能被 `inference.py` 的控制循环调用：

```python
class MyClient:
    def step(self, task_description=None, fps=None, **kwargs) -> np.ndarray:
        """单帧推理+执行，返回动作数组。"""
        ...

    def close(self):
        """释放资源（WebSocket 连接、后台线程等）。"""
        ...
```

### 机器人接口规范

所有机器人类必须实现以下方法，供 factory 和 `inference.py` 调用：

```python
class MyRobot:
    def connect(self):
        """建立硬件连接（相机、传感器等）。"""
        ...

    def disconnect(self):
        """断开所有硬件连接。"""
        ...
```

### 命名约定

- **注册名**：`<机器人类型>_<客户端名>`，如 `bimanual_ur_starvla`、`single_panda_dreamzero`
- **目录结构**：`robots/<机器人类型>/clients/<客户端名>_client.py`
- **Factory 函数**：使用 lazy import，只在被调用时才导入重依赖（确保注册阶段不需要硬件库）

### Lazy Import 原则

注册代码（`clients/__init__.py`）中的 factory 函数**必须**使用延迟导入：

```python
# 正确 ✓ — import 在 factory 内部，仅在实际创建时执行
def _my_factory(args):
    from .my_client import MyClient    # lazy import
    from ..config import MyConfig
    ...

# 错误 ✗ — 顶层 import 会在注册时就要求所有依赖已安装
from .my_client import MyClient        # 会导致缺依赖时注册失败
def _my_factory(args):
    ...
```

这保证了即使某个客户端的依赖未安装（如 `websockets`、`ur-rtde`），其他客户端仍能正常注册和使用。

---

## 硬件配置

机器人硬件参数定义在各自的 `config.py` 中。以 `bimanual_ur` 为例，修改 `BimanualURConfig` 的默认值以匹配你的设备：

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
```
