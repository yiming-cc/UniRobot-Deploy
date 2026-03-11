# 添加 save_data 参数说明

## 修改内容

在 `lerobot_record.py` 中添加了 `save_data` 参数，用于控制是否保存数据到数据集。

## 修改详情

### 1. DatasetRecordConfig 配置类

添加了新参数：
```python
# Whether to save data to dataset (default: False, only run robot without saving)
save_data: bool = False
```

**默认值**: `False` - 默认不保存数据，仅执行机器人动作

### 2. record_loop() 函数签名

添加了 `dataset_features` 参数：
```python
def record_loop(
    robot: Robot,
    events: dict,
    fps: int,
    teleop_action_processor: ...,
    robot_action_processor: ...,
    robot_observation_processor: ...,
    dataset_features: dict[str, Any],  # 新增：用于构建观测和动作帧
    dataset: LeRobotDataset | None = None,
    ...
)
```

**原因**: 当 `save_data=False` 时，`dataset=None`，但 policy 仍需要使用 `dataset_features` 来构建 observation_frame。

**修改点**:
- `build_dataset_frame(dataset.features, ...)` → `build_dataset_frame(dataset_features, ...)`
- `make_robot_action(action_values, dataset.features)` → `make_robot_action(action_values, dataset_features)`

### 3. record() 函数

修改了数据集创建和保存逻辑：

#### 数据集创建
- **当 `save_data=False`**:
  - 不创建数据集对象
  - 不启动图像写入器
  - 只运行机器人控制循环（执行动作但不保存）
  - 记录日志："save_data is False, running in execution-only mode (no dataset will be saved)"

- **当 `save_data=True`**:
  - 正常创建/加载数据集
  - 启动图像写入器
  - 保存所有观测和动作数据

#### Episode 保存
- **当 `save_data=False`**: 跳过 `dataset.save_episode()`
- **当 `save_data=True`**: 正常保存每个 episode

#### Hub 推送
- **当 `save_data=False`**: 跳过推送（没有数据集）
- **当 `save_data=True` 且 `push_to_hub=True`**: 推送到 Hugging Face Hub

### 3. 其他兼容性处理

- 添加了 `contextlib` 导入
- 使用 `contextlib.nullcontext()` 处理无数据集情况
- 所有涉及 `dataset` 的操作都添加了 `if dataset` 检查

## 使用方法

### 仅执行模式（默认）

```bash
python lerobot_record.py \
    --robot.type ur5e \
    --robot.robot_ip 192.168.1.100 \
    --robot.control_method joint \
    --dataset.repo_id ${HF_USER}/ur5e_demo \
    --dataset.single_task "Pick and place" \
    --dataset.save_data False \
    --policy.type xvla_client \
    --policy.url <YOUR_SERVER_URL>
```

**效果**: 机器人会执行策略动作，但不保存任何数据到数据集。适合用于部署和测试。

### 保存数据模式

```bash
python lerobot_record.py \
    --robot.type ur5e \
    --robot.robot_ip 192.168.1.100 \
    --robot.control_method joint \
    --dataset.repo_id ${HF_USER}/ur5e_demo \
    --dataset.single_task "Pick and place" \
    --dataset.save_data True \
    --dataset.push_to_hub True \
    --policy.type xvla_client \
    --policy.url <YOUR_SERVER_URL>
```

**效果**: 机器人执行策略动作，并保存所有数据到数据集，然后推送到 Hugging Face Hub。适合用于数据采集和模型训练。

## 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|-----|------|--------|------|
| `--dataset.save_data` | bool | False | 是否保存数据到数据集 |
| `--dataset.push_to_hub` | bool | True | 是否推送到 Hugging Face Hub（需要 save_data=True） |
| `--dataset.video` | bool | True | 是否将帧编码为视频（需要 save_data=True） |

## 使用场景

### 场景 1: 机器人部署（默认）
```bash
--dataset.save_data False
--dataset.push_to_hub False
```
- **用途**: 在生产环境中部署机器人
- **特点**: 不保存数据，只执行动作
- **优势**: 性能最优，无 I/O 开销

### 场景 2: 数据采集
```bash
--dataset.save_data True
--dataset.push_to_hub False
```
- **用途**: 收集数据但暂不上传
- **特点**: 保存到本地数据集
- **优势**: 可以先验证数据质量再决定是否上传

### 场景 3: 数据采集 + 自动上传
```bash
--dataset.save_data True
--dataset.push_to_hub True
```
- **用途**: 收集数据并自动上传到 Hub
- **特点**: 完整的数据采集流程
- **优势**: 自动化数据管理

## 性能影响

| 模式 | 数据集创建 | 图像写入 | 视频编码 | Hub 上传 | 性能影响 |
|-----|-----------|---------|---------|---------|---------|
| save_data=False | ✗ | ✗ | ✗ | ✗ | **最小** |
| save_data=True | ✓ | ✓ | ✓ | 可选 | 中等到高 |

**建议**:
- 部署时使用 `save_data=False` 获得最佳性能
- 数据采集时使用 `save_data=True`

## 向后兼容性

- **默认行为改变**: 原来默认会保存数据，现在默认不保存
- **迁移指南**: 如果需要保存数据，必须显式设置 `--dataset.save_data True`

## 示例脚本更新

所有运行脚本（如 `run_ur5e.sh`）已更新为明确指定 `--dataset.save_data False`。

## 注意事项

1. **Policy 需要 dataset.meta**:
   - 如果 policy 需要 dataset 的统计信息（stats），在 `save_data=False` 时可能会遇到问题
   - 当前实现使用 `dataset.meta if dataset else None` 来处理此情况

2. **record_loop 中的 observation_frame**:
   - 即使 `save_data=False`，仍然需要构建 observation_frame 给 policy 使用
   - 当前实现保留了这部分逻辑

3. **日志记录**:
   - 当 `save_data=False` 时，会记录特殊日志提示用户处于仅执行模式

## 测试建议

### 测试 1: 仅执行模式
```bash
python lerobot_record.py --dataset.save_data False [其他参数]
```
验证:
- [ ] 机器人正常执行动作
- [ ] 不创建数据集目录
- [ ] 无图像写入操作
- [ ] 日志显示 "execution-only mode"

### 测试 2: 保存数据模式
```bash
python lerobot_record.py --dataset.save_data True [其他参数]
```
验证:
- [ ] 机器人正常执行动作
- [ ] 创建数据集目录
- [ ] 保存图像和元数据
- [ ] Episode 正常保存

---

**修改完成时间**: 2026-03-11
**修改文件**: `lerobot_record.py`, `run_ur5e.sh`
