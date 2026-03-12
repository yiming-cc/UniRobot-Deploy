# DreamZero 对接文档

## 1. 背景与动机

DreamZeroClient 用于对接 DreamZero 推理服务端（`socket_test_optimized_AR.py`）。原实现基于 OpenPI 协议（继承 `WebsocketClientPolicy`），无法直接对接 DreamZero 服务端，核心差异：

| 差异点 | OpenPI 协议 | DreamZero 协议 |
|--------|------------|----------------|
| 多帧机制 | 每次 1 帧 | 首次 1 帧，后续 4 帧 |
| 图像分辨率 | 224×224 (pad) | 180×320 (resize) |
| 状态格式 | `observation/state` (28D 合并) | 4 个独立 key（各 7D） |
| 会话管理 | 无 | `session_id` (UUID) |
| 推理入口 | `infer()` 由父类封装 | 需手动添加 `endpoint="infer"` |
| 返回格式 | `{"actions": ndarray}` dict | 直接返回 `np.ndarray` |
| 动作维度顺序 | `[tcp(14), joints(14)]` | `[left_joints(7), right_joints(7), left_tcp(7), right_tcp(7)]` |

因此需要完全重写，去掉 `WebsocketClientPolicy` 继承，自建通信层。

---

## 2. DreamZero 通信协议

### WebSocket + msgpack 协议

- 传输层：`websockets.sync.client` + `openpi_client.msgpack_numpy` 序列化
- 连接参数：`compression=None, max_size=None, ping_interval=60, ping_timeout=600`
  - 长 timeout 是为了容忍首次推理 30-80s 模型预热
- 服务端首条消息：连接后立即接收 metadata dict（`msgpack_numpy.unpackb(ws.recv())`）

### endpoint 字段

每次请求需在 obs dict 中设置 `endpoint` 字段：

```python
# 推理请求
obs["endpoint"] = "infer"
ws.send(packer.pack(obs))
actions = msgpack_numpy.unpackb(ws.recv())  # np.ndarray (24, 28)

# 重置请求
info["endpoint"] = "reset"
ws.send(packer.pack(info))
ws.recv()  # 服务端确认
```

### 重连机制

推理支持 3 次重试，每次失败后自动重连 WebSocket。

---

## 3. 数据格式

### 观测 dict（客户端 → 服务端）

```python
{
    # ── 图像观测 ──
    # 首次推理: (180, 320, 3) uint8
    # 后续推理: (4, 180, 320, 3) uint8
    "observation/top":     np.ndarray,
    "observation/wrist_l": np.ndarray,
    "observation/wrist_r": np.ndarray,

    # ── 状态观测（4 个独立 key） ──
    "observation/left_joint_positions":  np.ndarray,  # (7,) = 6 joints + gripper
    "observation/right_joint_positions": np.ndarray,  # (7,)
    "observation/left_ee_pos_rot":      np.ndarray,  # (7,) = 6D pose + gripper
    "observation/right_ee_pos_rot":     np.ndarray,  # (7,)

    # ── 元信息 ──
    "prompt":     str,   # 任务描述
    "session_id": str,   # UUID，同一 episode 内不变
    "endpoint":   "infer",
}
```

### 动作返回（服务端 → 客户端）

服务端直接返回 `np.ndarray`，shape `(24, 28)`。

28 维动作顺序（与 EMBODIMENT_CONFIGS 的 action_keys 一致）：

| 索引 | 内容 | 来源 |
|------|------|------|
| 0-6 | left_joint_positions (6 joints + gripper) | 左臂关节 |
| 7-13 | right_joint_positions (6 joints + gripper) | 右臂关节 |
| 14-20 | left_ee_pos_rot (6D pose + gripper) | 左臂 TCP |
| 21-27 | right_ee_pos_rot (6D pose + gripper) | 右臂 TCP |

执行映射：
- `action_type="joint"`: 使用 `[0:7]` 和 `[7:14]`
- `action_type="tcp"`: 使用 `[14:21]` 和 `[21:28]`

---

## 4. 多帧机制详解

### 常量

```python
ACTION_HORIZON = 24           # 每次推理返回 24 步动作
IMAGE_WIDTH = 320
IMAGE_HEIGHT = 180
FRAME_INDICES = [0, 7, 15, 23]  # 对应 RELATIVE_OFFSETS = [-23, -16, -8, 0]
```

### 帧缓冲

每个相机维护 `deque(maxlen=24)`，每次 `step()` 捕获当前帧并 resize 到 180×320 后入队。

内存占用：3 相机 × 24 帧 × 180×320×3 ≈ 12MB，可忽略。

### 调度逻辑

**首次推理**（`_is_first_inference=True`）：
- 发送 1 帧 `(H, W, 3)` — 取 buffer 最新帧
- 此时 buffer 可能不足 24 帧（只有 1 帧）

**后续推理**：
- 每次推理恰好在执行完 24 步后触发（action_queue 耗尽）
- 此时 buffer 恰好有 24 帧
- 从 buffer 按 `FRAME_INDICES = [0, 7, 15, 23]` 取 4 帧
- 发送 `(4, H, W, 3)` 的 stacked array

### 时序示意

```
step  0: 捕获帧 → buffer=[f0]      → 首次推理(1帧) → 获得24动作 → 执行 a[0]
step  1: 捕获帧 → buffer=[f0,f1]   → 从缓存执行 a[1]
step  2: 捕获帧 → buffer=[f0..f2]  → 从缓存执行 a[2]
...
step 23: 捕获帧 → buffer=[f0..f23] → 从缓存执行 a[23]
step 24: 捕获帧 → buffer=[f1..f24] → 队列空 → 4帧推理(indices[0,7,15,23]) → 获得24动作
step 25: 捕获帧 → buffer=[f2..f25] → 从缓存执行
...
```

---

## 5. 会话管理

### session_id 生命周期

1. **初始化**: `__init__` 中生成 `uuid.uuid4()`
2. **每次推理**: 随 obs dict 发送给服务端
3. **重置**: `reset()` 时生成新 UUID，通知服务端（服务端保存视频并清理状态）
4. **关闭**: `close()` 时发送最终 reset

### reset 触发时机

- `step()` 中检测到 `task_description` 变化时自动触发
- 外部显式调用 `client.reset(task_description)`

### reset 操作

```python
def reset(self, task_description=None):
    self._session_id = str(uuid.uuid4())  # 新会话
    self.action_queue.clear()             # 清空动作缓存
    for buf in self._frame_buffer.values():
        buf.clear()                       # 清空帧缓冲
    self._global_step = 0
    self._is_first_inference = True       # 下次推理发 1 帧
    self._reset_ws({"session_id": ...})   # 通知服务端
```

---

## 6. 使用方式

### 启动命令

```bash
# 启动 DreamZero 服务端
python socket_test_optimized_AR.py --embodiment bimanual_ur

# 启动客户端推理（需连接硬件）
python inference.py \
    --client=bimanual_ur_dreamzero \
    --host="ws://<server_ip>:<port>/ws" \
    --task="pick up the red cup" \
    --fps=30 \
    --verbose

# 参数说明
#   --client          选择 DreamZero 客户端
#   --host            服务端 WebSocket 地址
#   --task            任务描述（语言指令）
#   --fps             控制频率（默认 30Hz）
#   --action_type     joint（关节空间）或 tcp（笛卡尔空间）
#   --verbose         打印推理时间、动作维度等详细日志
```

### 与服务端配合流程

```
1. 服务端启动，等待 WebSocket 连接
2. 客户端连接，接收 metadata
3. 客户端发送首次推理（1帧 + 状态 + prompt + session_id）
4. 服务端返回 (24, 28) 动作数组
5. 客户端按 30Hz 执行 24 步
6. 第 25 步：客户端发送 4 帧推理请求
7. 循环 4-6，直到任务完成
8. 任务切换时发送 reset，服务端保存视频
```

---

## 7. 调试指南

### WebSocket 超时

**现象**: 连接成功但首次推理长时间无响应

**原因**: 模型首次推理需要 30-80s 预热（JIT 编译等）

**解决**: `ping_timeout=600` 已配置。如仍超时，检查服务端日志确认模型是否正常加载。

### 帧调度错位

**现象**: 后续推理发送帧数不对，或索引越界

**检查点**:
1. 确认 `ACTION_HORIZON = 24` 与服务端返回的动作步数一致
2. 确认 `FRAME_INDICES = [0, 7, 15, 23]` 均 < buffer maxlen
3. 检查 `_is_first_inference` 标志是否在首次推理后正确设为 `False`
4. 检查 `reset()` 是否清空了 frame_buffer

### 动作维度错误

**现象**: 机器人动作异常（关节和 TCP 混淆）

**检查点**:
1. 确认 `action_type` 参数正确：`joint` 用 `[0:7]`+`[7:14]`，`tcp` 用 `[14:21]`+`[21:28]`
2. 确认服务端返回 shape 为 `(24, 28)`
3. 打印首个动作值，与服务端日志对比

### 连接断开

**现象**: 推理过程中突然失败

**处理**: 客户端自动重试 3 次并重连。若持续失败：
1. 检查网络连通性 (`ping <server_ip>`)
2. 检查服务端是否仍在运行
3. 检查是否有防火墙/代理干扰（客户端已清除 `*_PROXY` 环境变量）

### session_id 不一致

**现象**: 服务端报 session 不存在

**检查点**:
1. `reset()` 会生成新 UUID，确认不是意外触发了 reset
2. 检查 task_description 是否在每次 `step()` 调用时变化（会触发自动 reset）
3. 日志中搜索 "Session reset" 确认 reset 调用时机
