# DreamZeroClient 数据格式

## 概述

DreamZeroClient 使用标准 openpi WebSocket 协议与远程推理服务器通信。数据通过 msgpack + numpy 序列化传输。

---

## 发送数据（客户端 → 服务器）

`step()` 每帧调用 `_build_observation()` 构建观测字典，当 action queue 为空时通过 `infer(obs)` 发送给服务器。

### 观测字典结构

```python
{
    # ── 图像观测 ──
    # 每个相机一个 key，名称来自 config.camera_serial_numbers 的 key
    # 图像经过 resize_with_pad(224, 224) + convert_to_uint8 处理
    "observation/top":     np.ndarray,  # shape: (224, 224, 3), dtype: uint8
    "observation/wrist_l": np.ndarray,  # shape: (224, 224, 3), dtype: uint8
    "observation/wrist_r": np.ndarray,  # shape: (224, 224, 3), dtype: uint8

    # ── 状态观测 ──
    # 拼接顺序: [left_tcp(7), right_tcp(7), left_joints(7), right_joints(7)]
    #   tcp = [x, y, z, rx, ry, rz, gripper]  (位姿 6D + 夹爪 1D)
    #   joints = [j0, j1, j2, j3, j4, j5, gripper]  (关节角 6D + 夹爪 1D)
    "observation/state": np.ndarray,  # shape: (28,), dtype: float64

    # ── 任务指令 ──
    "prompt": str,  # 例如 "pick up the red cup"
}
```

### 图像处理流程

```
原始图像 (640×480, uint8)
  → image_tools.resize_with_pad(img, 224, 224)   # 等比缩放 + 零填充
  → image_tools.convert_to_uint8(img)             # 确保 uint8 格式
  → 最终图像 (224×224, uint8)
```

### 状态向量 (28D) 分解

| 索引 | 内容 | 来源 |
|------|------|------|
| 0-6 | 左臂 TCP (x,y,z,rx,ry,rz,gripper) | `left_arm.get_tcp_state()` |
| 7-13 | 右臂 TCP (x,y,z,rx,ry,rz,gripper) | `right_arm.get_tcp_state()` |
| 14-20 | 左臂关节角 (j0-j5,gripper) | `left_arm.get_joint_state()` |
| 21-27 | 右臂关节角 (j0-j5,gripper) | `right_arm.get_joint_state()` |

### 传输协议

```
观测字典 → msgpack_numpy.pack() → WebSocket binary frame → 服务器
```

---

## 接收数据（服务器 → 客户端）

服务器返回 msgpack 序列化的字典，客户端通过 `msgpack_numpy.unpackb()` 解包。

### 响应字典结构

```python
{
    "actions": np.ndarray,  # shape: (action_horizon, action_dim)
                            # 即 (H, 28)，H 为服务器配置的 action chunk 长度
}
```

### Action Chunk 详解

每个 action 是 28 维向量，布局与 StarVLAClient 一致：

| 索引 | 内容 |
|------|------|
| 0-13 | TCP 动作: [left_tcp(7), right_tcp(7)] |
| 14-27 | 关节动作: [left_joints(7), right_joints(7)] |

实际使用哪部分取决于 `action_type` 参数：
- `action_type="joint"` → 使用索引 14-27（关节角）
- `action_type="tcp"` → 使用索引 0-13（TCP 位姿）

### Action Chunk 缓存机制

```
服务器返回 actions (H, 28)
  → 全部入队 action_queue
  → 每次 step() 消费 1 个
  → 队列为空时再请求服务器

时序示意 (假设 action_horizon=10, fps=30):
  step 0:  请求服务器 → 获得 10 个动作 → 执行第 0 个
  step 1:  从缓存取第 1 个 → 执行
  step 2:  从缓存取第 2 个 → 执行
  ...
  step 9:  从缓存取第 9 个 → 执行
  step 10: 队列为空 → 请求服务器 → 获得新的 10 个动作 → 执行第 0 个
```

---

## 与 StarVLAClient 数据格式对比

| | DreamZeroClient | StarVLAClient |
|---|---|---|
| **发送图像** | `np.ndarray` (224×224 uint8) | JPEG bytes (`cv2.imencode`) |
| **图像 key** | `observation/<cam_name>` | `batch_images` (嵌套列表) |
| **状态 key** | `observation/state` (28D flat) | `state` (1×28 带 batch 维度) |
| **指令 key** | `prompt` | `instructions` |
| **包装格式** | 直接发送 obs dict | `{"payload": obs, "type": "infer"}` |
| **响应解析** | `response["actions"]` | `response["data"]["actions"][0]` |
