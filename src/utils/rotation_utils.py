
from scipy.spatial.transform import Rotation as R
import numpy as np

class RotationConverter:
    """
    一个用于在 Axis-Angle (旋转向量), Rotate6D, Quaternion (x,y,z,w), Matrix 和 Euler (x,y,z)
    之间进行转换的工具类。
    
    支持批量 (Batch) 操作。
    所有输入输出均为 numpy.array。
    """

    @staticmethod
    def _normalize(tensor, eps=1e-12):
        """辅助函数：归一化向量，防止除零"""
        norm = np.linalg.norm(tensor, axis=-1, keepdims=True)
        return tensor / (norm + eps)

    @staticmethod
    def _rotate6d_to_matrix(d6, row_concat=False):
        """
        核心逻辑：将 6D 旋转表示转换为 3x3 旋转矩阵。
        使用 Gram-Schmidt 正交化过程。
        
        Args:
            d6: shape (..., 6) 的 numpy 数组
        Returns:
            matrix: shape (..., 3, 3) 的旋转矩阵
        """
        # 1. 提取两个 3D 向量
        a1 = d6[..., 0:5:2] if row_concat else d6[..., 0:3] 
        a2 = d6[..., 1:6:2] if row_concat else d6[..., 3:6]

        # 2. 归一化第一个向量
        b1 = RotationConverter._normalize(a1)

        # 3. 对第二个向量进行正交化 (Gram-Schmidt)
        # b2 = a2 - proj_{b1}(a2)
        proj = np.sum(a2 * b1, axis=-1, keepdims=True) * b1
        b2 = a2 - proj
        b2 = RotationConverter._normalize(b2)

        # 4. 通过叉乘计算第三个向量
        b3 = np.cross(b1, b2, axis=-1)

        # 5. 堆叠成旋转矩阵 (..., 3, 3)
        # 这里的向量是矩阵的列向量
        return np.stack((b1, b2, b3), axis=-1)

    @staticmethod
    def _matrix_to_rotate6d(matrix, row_concat=False):
        """
        核心逻辑：将 3x3 旋转矩阵转换为 6D 表示。
        直接取矩阵的前两列并展平。
        
        Args:
            matrix: shape (..., 3, 3)
        Returns:
            d6: shape (..., 6)

        [[a00, a01, a02]
         [a10, a11, a12]
         [a20, a21, a22]]
        if row_concat: [a00, a01, a10, a11, a20, a21]
        else: [a00, a10, a20, a01, a11, a21]
        """
        if row_concat:
            # 提取前两列并按行展平: [a00, a01, a10, a11, a20, a21]
            rot6d = matrix[..., :, :2].reshape(*matrix.shape[:-2], -1)
        else:
            m0 = matrix[..., :, 0]
            m1 = matrix[..., :, 1]
            rot6d = np.concatenate([m0, m1], axis=-1)
        return rot6d

    # =================================================================
    #                          API 接口函数
    # =================================================================

    @staticmethod
    def rotate6d_to_quaternion(d6, row_concat=False):
        """
        将 6D 旋转转换为四元数 (x, y, z, w)。
        Args:
            d6: (N, 6) 或 (6,)
        Returns:
            quat: (N, 4) 或 (4,)
        """
        d6 = np.asarray(d6)
        matrix = RotationConverter._rotate6d_to_matrix(d6, row_concat)
        # 使用 scipy 将矩阵转为四元数，默认顺序为 (x, y, z, w)
        return R.from_matrix(matrix).as_quat()

    @staticmethod
    def quaternion_to_rotate6d(quat, row_concat=False):
        """
        将四元数 (x, y, z, w) 转换为 6D 旋转。
        Args:
            quat: (N, 4) 或 (4,)
        Returns:
            d6: (N, 6) 或 (6,)
        """
        quat = np.asarray(quat)
        # 归一化四元数是个好习惯，尽管 scipy 会处理
        matrix = R.from_quat(quat).as_matrix()
        return RotationConverter._matrix_to_rotate6d(matrix, row_concat)

    @staticmethod
    def axis_angle_to_rotate6d(axis_angle, row_concat=False):
        """
        将轴角 (旋转向量) 转换为 6D 旋转。
        Args:
            axis_angle: (N, 3) 或 (3,)。模长为角度(弧度)，方向为轴。
        Returns:
            d6: (N, 6) 或 (6,)
        """
        axis_angle = np.asarray(axis_angle)
        matrix = R.from_rotvec(axis_angle).as_matrix()
        return RotationConverter._matrix_to_rotate6d(matrix, row_concat)

    @staticmethod
    def rotate6d_to_axis_angle(d6, row_concat=False):
        """
        将 6D 旋转转换为轴角 (旋转向量)。
        Args:
            d6: (N, 6) 或 (6,)
        Returns:
            axis_angle: (N, 3) 或 (3,)
        """
        d6 = np.asarray(d6)
        matrix = RotationConverter._rotate6d_to_matrix(d6, row_concat)
        return R.from_matrix(matrix).as_rotvec()

    @staticmethod
    def axis_angle_to_quaternion(axis_angle):
        """
        将轴角转换为四元数 (x, y, z, w)。
        Args:
            axis_angle: (N, 3)
        Returns:
            quat: (N, 4)
        """
        axis_angle = np.asarray(axis_angle)
        return R.from_rotvec(axis_angle).as_quat()

    @staticmethod
    def quaternion_to_axis_angle(quat):
        """
        将四元数 (x, y, z, w) 转换为轴角。
        Args:
            quat: (N, 4)
        Returns:
            axis_angle: (N, 3)
        """
        quat = np.asarray(quat)
        return R.from_quat(quat).as_rotvec()

    @staticmethod
    def axis_angle_to_matrix(axis_angle):
        """
        将轴角 (旋转向量) 转换为 3x3 旋转矩阵。
        Args:
            axis_angle: (N, 3)
        Returns:
            matrix: (N, 3, 3)
        """
        axis_angle = np.asarray(axis_angle)
        return R.from_rotvec(axis_angle).as_matrix()
    
    @staticmethod
    def matrix_to_axis_angle(matrix):
        """
        将 3x3 旋转矩阵转换为轴角 (旋转向量)。
        Args:
            matrix: (N, 3, 3)
        Returns:
            axis_angle: (N, 3)
        """
        matrix = np.asarray(matrix)
        return R.from_matrix(matrix).as_rotvec()

    @staticmethod
    def rotate6d_to_matrix(d6):
        """
        将 6D 旋转转换为 3x3 旋转矩阵。
        Args:
            d6: (N, 6) or (6,)
        Returns:
            matrix: (N, 3, 3) or (3, 3)
        """
        d6 = np.asarray(d6)
        return RotationConverter._rotate6d_to_matrix(d6)
    
    @staticmethod
    def matrix_to_rotate6d(matrix, row_concat=False):
        """
        将 3x3 旋转矩阵转换为 6D 旋转。
        Args:
            matrix: (N, 3, 3) or (3, 3)
        Returns:
            d6: (N, 6) or (6,)
        """
        matrix = np.asarray(matrix)
        return RotationConverter._matrix_to_rotate6d(matrix, row_concat)
    
    @staticmethod
    def matrix_to_quaternion(matrix):
        """
        将 3x3 旋转矩阵转换为四元数 (x, y, z, w)。
        Args:
            matrix: (N, 3, 3) or (3, 3)
        Returns:
            quat: (N, 4) or (4,)
        """
        matrix = np.asarray(matrix)
        return R.from_matrix(matrix).as_quat()
    
    @staticmethod
    def quaternion_to_matrix(quat):
        """
        将四元数 (x, y, z, w) 转换为 3x3 旋转矩阵。
        Args:
            quat: (N, 4) or (4,)
        Returns:
            matrix: (N, 3, 3) or (3, 3)
        """
        quat = np.asarray(quat)
        return R.from_quat(quat).as_matrix()

    @staticmethod
    def matrix_to_euler(matrix):
        """
        将 3x3 旋转矩阵转换为欧拉角 (x, y, z)。
        Args:
            matrix: (N, 3, 3) or (3, 3)
        Returns:
            euler: (N, 3) or (3,)
        """
        matrix = np.asarray(matrix)
        return R.from_matrix(matrix).as_euler('xyz', degrees=False)
    
    @staticmethod
    def euler_to_matrix(euler):
        """
        将欧拉角 (x, y, z) 转换为 3x3 旋转矩阵。
        Args:
            euler: (N, 3) or (3,)
        Returns:
            matrix: (N, 3, 3) or (3, 3)
        """
        euler = np.asarray(euler)
        return R.from_euler('xyz', euler, degrees=False).as_matrix()
    
    @staticmethod
    def euler_to_quaternion(euler):
        """
        将欧拉角 (x, y, z) 转换为四元数 (x, y, z, w)。
        Args:
            euler: (N, 3) or (3,)
        Returns:
            quat: (N, 4) or (4,)
        """
        euler = np.asarray(euler)
        return R.from_euler('xyz', euler, degrees=False).as_quat()
    
    @staticmethod
    def quaternion_to_euler(quat):
        """
        将四元数 (x, y, z, w) 转换为欧拉角 (x, y, z)。
        Args:
            quat: (N, 4) or (4,)
        Returns:
            euler: (N, 3) or (3,)
        """
        quat = np.asarray(quat)
        return R.from_quat(quat).as_euler('xyz', degrees=False)
    
    @staticmethod
    def rotate6d_to_euler(d6, row_concat=False):
        """
        将 6D 旋转转换为欧拉角 (x, y, z)。
        Args:
            d6: (N, 6) or (6,)
        Returns:
            euler: (N, 3) or (3,)
        """
        d6 = np.asarray(d6)
        matrix = RotationConverter._rotate6d_to_matrix(d6, row_concat)
        return R.from_matrix(matrix).as_euler('xyz', degrees=False)
    
    @staticmethod
    def euler_to_rotate6d(euler, row_concat=False):
        """
        将欧拉角 (x, y, z) 转换为 6D 旋转。
        Args:
            euler: (N, 3) or (3,)
        Returns:
            d6: (N, 6) or (6,)
        """
        euler = np.asarray(euler)
        matrix = R.from_euler('xyz', euler, degrees=False).as_matrix()
        return RotationConverter._matrix_to_rotate6d(matrix, row_concat)
    
    @staticmethod
    def axis_angle_to_euler(axis_angle):
        """
        将轴角 (旋转向量) 转换为欧拉角 (x, y, z)。
        Args:
            axis_angle: (N, 3) or (3,)
        Returns:
            euler: (N, 3) or (3,)
        """
        axis_angle = np.asarray(axis_angle)
        return R.from_rotvec(axis_angle).as_euler('xyz', degrees=False)
    
    @staticmethod
    def euler_to_axis_angle(euler):
        """
        将欧拉角 (x, y, z) 转换为轴角 (旋转向量)。
        Args:
            euler: (N, 3) or (3,)
        Returns:
            axis_angle: (N, 3) or (3,)
        """
        euler = np.asarray(euler)
        return R.from_euler('xyz', euler, degrees=False).as_rotvec()