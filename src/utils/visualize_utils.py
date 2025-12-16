import numpy as np
import matplotlib
# 使用非交互式后端，避免 tkinter 线程问题
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R

def visualize_action_chunk_to_video(action_chunk, output_path='robot_action.mp4', fps=30, triad_scale=0.1):
    """
    将 [N, 7] 的 action chunk 可视化为 MP4 视频。
    
    Args:
        action_chunk (np.array): 形状为 [N, 7]。
                                 前3维: (x, y, z) position
                                 后4维: (x, y, z, w) quaternion
        output_path (str): 输出 mp4 文件的路径。
        fps (int): 视频帧率。
        triad_scale (float): RGB 坐标轴箭头的长度，根据轨迹范围调整大小。
    """
    
    # 1. 数据解析
    N = action_chunk.shape[0]
    positions = action_chunk[:, :3]  # (N, 3)
    quaternions = action_chunk[:, 3:] # (N, 4) -> (x, y, z, w)

    # 将四元数转换为旋转矩阵，用于提取坐标轴方向
    # scipy 默认 quat 顺序为 (x, y, z, w)
    r = R.from_quat(quaternions)
    rot_matrices = r.as_matrix()  # (N, 3, 3)

    # 2. 设置绘图窗口
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 设置标题和轴标签
    ax.set_title(f"Robot End-Effector Trajectory (N={N})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # 3. 自动计算坐标轴范围 (防止镜头晃动)
    # 找到所有点的最大最小值，并留出一点余量
    min_xyz = np.min(positions, axis=0)
    max_xyz = np.max(positions, axis=0)
    mid_xyz = (min_xyz + max_xyz) / 2
    max_range = np.max(max_xyz - min_xyz) / 2
    
    # 为了保持 1:1:1 的比例，所有轴都使用最大的那个范围
    # (Matplotlib 3D 默认比例通常不是 1:1，这里强制调整)
    padding = max_range * 1.2 + triad_scale # 加上箭头长度作为缓冲
    ax.set_xlim(mid_xyz[0] - padding, mid_xyz[0] + padding)
    ax.set_ylim(mid_xyz[1] - padding, mid_xyz[1] + padding)
    ax.set_zlim(mid_xyz[2] - padding, mid_xyz[2] + padding)

    # 4. 初始化绘图元素
    # 轨迹线 (初始为空)
    line, = ax.plot([], [], [], 'k--', linewidth=1, label='Path', alpha=0.5)
    # 当前位置的点
    point, = ax.plot([], [], [], 'ko', markersize=4)
    
    # 用于存储当前帧的三轴箭头 (quiver对象)
    # 列表顺序: [X_arrow, Y_arrow, Z_arrow]
    current_triad = []

    def update(frame):
        nonlocal current_triad
        
        # --- A. 更新轨迹线 ---
        # 绘制从第0帧到当前帧的路径
        line.set_data(positions[:frame+1, 0], positions[:frame+1, 1])
        line.set_3d_properties(positions[:frame+1, 2])
        
        # --- B. 更新当前点 ---
        point.set_data([positions[frame, 0]], [positions[frame, 1]])
        point.set_3d_properties([positions[frame, 2]])
        
        # --- C. 更新姿态三轴 (RGB Triad) ---
        # 清除上一帧的箭头
        for arrow in current_triad:
            arrow.remove()
        current_triad = []
        
        # 获取当前位置和旋转矩阵
        pos = positions[frame]
        rot_mat = rot_matrices[frame] # 3x3
        
        # 旋转矩阵的列向量分别对应局部坐标系的 X, Y, Z 轴在世界坐标系下的方向
        x_dir = rot_mat[:, 0]
        y_dir = rot_mat[:, 1]
        z_dir = rot_mat[:, 2]
        
        # 绘制三个箭头 (quiver)
        # 参数: x, y, z, u, v, w, color
        # 红色 X轴
        q_x = ax.quiver(pos[0], pos[1], pos[2], 
                        x_dir[0], x_dir[1], x_dir[2], 
                        length=triad_scale, color='r', normalize=True)
        # 绿色 Y轴
        q_y = ax.quiver(pos[0], pos[1], pos[2], 
                        y_dir[0], y_dir[1], y_dir[2], 
                        length=triad_scale, color='g', normalize=True)
        # 蓝色 Z轴
        q_z = ax.quiver(pos[0], pos[1], pos[2], 
                        z_dir[0], z_dir[1], z_dir[2], 
                        length=triad_scale, color='b', normalize=True)
        
        current_triad = [q_x, q_y, q_z]
        
        return line, point

    print(f"开始生成动画，共 {N} 帧...")
    
    # 创建动画对象
    ani = None
    try:
        ani = animation.FuncAnimation(fig, update, frames=N, interval=1000/fps, blit=False)
        
        # 保存视频
        # 需要系统安装 ffmpeg。如果没有，可以尝试改为 writer='pillow' 保存为 .gif
        try:
            writer = animation.FFMpegWriter(fps=fps, metadata=dict(artist='Me'), bitrate=1800)
            ani.save(output_path, writer=writer)
            print(f"成功保存视频至: {output_path}")
        except Exception as e:
            print(f"保存 MP4 失败 (通常是因为未安装 ffmpeg): {e}")
            print("尝试保存为 GIF...")
            try:
                ani.save(output_path.replace('.mp4', '.gif'), writer='pillow', fps=fps)
                print(f"已保存为 GIF: {output_path.replace('.mp4', '.gif')}")
            except Exception as e_gif:
                print(f"保存 GIF 也失败了: {e_gif}")
    finally:
        # 确保清理所有资源
        if ani is not None:
            ani.event_source.stop()  # 停止动画事件源
        plt.close(fig)  # 关闭 figure
        plt.close('all')  # 关闭所有 figure，确保完全清理

# ==========================================
# 测试代码
# ==========================================
# if __name__ == "__main__":
#     # 生成一段模拟数据：螺旋上升 + 旋转
#     N_frames = 100
#     t = np.linspace(0, 4*np.pi, N_frames)
    
#     # 1. 位置: 螺旋上升
#     x = np.cos(t) * 0.5
#     y = np.sin(t) * 0.5
#     z = np.linspace(0, 1, N_frames)
#     positions = np.stack([x, y, z], axis=1)
    
#     # 2. 姿态: 绕 Z 轴持续旋转，同时稍微倾斜
#     # 使用 scipy 生成旋转
#     euler_angles = np.stack([t*0.5, t*0.0, t], axis=1) # 变动的欧拉角
#     quats = R.from_euler('xyz', euler_angles).as_quat() # (N, 4) -> (x,y,z,w)
    
#     # 3. 组合成 [N, 7]
#     action_chunk_sim = np.concatenate([positions, quats], axis=1)
    
#     # 执行可视化
#     visualize_action_chunk_to_video(action_chunk_sim, "robot_trajectory_viz.mp4", fps=30, triad_scale=0.2)