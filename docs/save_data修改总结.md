# save_data 参数修改总结

## ✅ 修改完成

已成功在 `lerobot_record.py` 中添加 `save_data` 参数，用于控制是否保存数据到数据集。

## 📝 修改的文件

1. **lerobot_record.py** - 主要修改
   - 添加 `contextlib` 导入
   - `DatasetRecordConfig` 类：添加 `save_data: bool = False` 参数
   - `record_loop()` 函数：添加 `dataset_features` 参数，修改三处使用 `dataset.features` 的代码
   - `record()` 函数：根据 `save_data` 条件创建数据集，添加空上下文管理器处理

2. **run_ur5e.sh** - 运行脚本
   - 添加 `--dataset.save_data False` 参数
   - 添加使用说明注释

3. **docs/save_data参数说明.md** - 完整文档
   - 详细说明修改内容和使用方法

## 🎯 核心改动

### 参数定义
```python
@dataclass
class DatasetRecordConfig:
    save_data: bool = False  # 默认不保存
```

### 数据集创建逻辑
```python
dataset = None
if cfg.dataset.save_data:
    # 创建或加载数据集
    dataset = LeRobotDataset.create(...)
else:
    logging.info("save_data is False, running in execution-only mode")
```

### 数据保存逻辑
```python
# 只在 dataset 存在时保存
if dataset:
    dataset.save_episode()

if dataset and cfg.dataset.push_to_hub:
    dataset.push_to_hub(...)
```

### record_loop 修改
```python
# 添加 dataset_features 参数，避免访问 dataset.features
def record_loop(..., dataset_features: dict[str, Any], dataset: LeRobotDataset | None = None, ...):
    ...
    # 使用 dataset_features 而不是 dataset.features
    observation_frame = build_dataset_frame(dataset_features, obs_processed, prefix=OBS_STR)
    act_processed_policy = make_robot_action(action_values, dataset_features)
    action_frame = build_dataset_frame(dataset_features, action_values, prefix=ACTION)
```

## 📖 使用方法

### 仅执行模式（默认，推荐用于部署）
```bash
python lerobot_record.py \
    --robot.type ur5e \
    --dataset.save_data False \
    --policy.type xvla_client \
    --policy.url <SERVER_URL>
```

### 数据采集模式
```bash
python lerobot_record.py \
    --robot.type ur5e \
    --dataset.save_data True \
    --dataset.push_to_hub True \
    --policy.type xvla_client \
    --policy.url <SERVER_URL>
```

## ⚡ 性能影响

| 模式 | I/O 操作 | 磁盘占用 | 性能 |
|-----|---------|---------|------|
| `save_data=False` | 无 | 0 GB | 最优 |
| `save_data=True` | 图像写入 + 视频编码 | 取决于 episode 数量 | 中等 |

## ✅ 验证结果

- [x] Python 语法检查通过
- [x] 所有 `dataset.features` 引用已修改为 `dataset_features`
- [x] 添加了空上下文管理器处理 `dataset=None` 情况
- [x] 更新了运行脚本和文档

## 🚀 下一步

使用以下命令测试：

**测试 1: 仅执行模式**
```bash
bash run_ur5e.sh
```
预期：机器人执行动作，不创建数据集目录，日志显示 "execution-only mode"

**测试 2: 保存数据模式**
```bash
# 修改 run_ur5e.sh 中的 --dataset.save_data True
bash run_ur5e.sh
```
预期：机器人执行动作，创建数据集目录，保存所有数据

## 📌 注意事项

1. **默认行为改变**: 原来默认会保存数据，现在默认不保存
2. **Policy 兼容性**: Policy 需要 `dataset_features` 来构建 observation_frame，即使在 `save_data=False` 时也会正常工作
3. **向后兼容**: 旧脚本需要显式添加 `--dataset.save_data True` 来保存数据

---

**修改完成时间**: 2026-03-11
**测试状态**: 待硬件测试
**文档状态**: 完整
