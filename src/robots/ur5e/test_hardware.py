#!/usr/bin/env python
"""
UR5e 硬件连接测试脚本

用于验证 RTDE、夹爪、摄像头是否正常连接。
"""

import sys

def test_rtde():
    """测试 RTDE 连接"""
    print("\n=== 测试 RTDE 连接 ===")
    try:
        import rtde_receive
        print("✓ ur_rtde 库已安装")

        robot_ip = "192.168.1.100"
        print(f"尝试连接到 {robot_ip}...")
        r = rtde_receive.RTDEReceiveInterface(robot_ip)

        joints = r.getActualQ()
        print(f"✓ RTDE 连接成功")
        print(f"  当前关节角度: {[f'{j:.3f}' for j in joints]}")

        tcp = r.getActualTCPPose()
        print(f"  当前 TCP 姿态: {[f'{t:.3f}' for t in tcp]}")

        return True
    except ImportError:
        print("✗ ur_rtde 库未安装")
        print("  安装命令: pip install ur_rtde")
        return False
    except Exception as e:
        print(f"✗ RTDE 连接失败: {e}")
        print("  请检查:")
        print("  1. 网络连接: ping 192.168.1.100")
        print("  2. UR 机器人是否启动")
        print("  3. RTDE 接口是否启用")
        return False

def test_gripper():
    """测试 Robotiq 夹爪"""
    print("\n=== 测试 Robotiq 夹爪 ===")
    try:
        import serial
        print("✓ pyserial 库已安装")

        gripper_port = "/dev/ttyUSB1"
        print(f"尝试连接到 {gripper_port}...")

        import os
        if not os.path.exists(gripper_port):
            print(f"✗ 串口设备 {gripper_port} 不存在")
            print("  请检查:")
            print("  1. USB 转串口是否连接")
            print("  2. 运行 dmesg | grep ttyUSB 查看设备")
            return False

        # 检查权限
        if not os.access(gripper_port, os.R_OK | os.W_OK):
            print(f"✗ 串口设备 {gripper_port} 无访问权限")
            print("  解决方法:")
            print(f"  sudo usermod -aG dialout $USER")
            print("  然后注销并重新登录")
            return False

        # 尝试初始化夹爪
        from src.robots.ur5e.robotiq import CtrlGrp
        print("正在激活夹爪（可能需要几秒）...")
        gripper = CtrlGrp(gripper_port)
        gripper.ACT()

        print("✓ 夹爪激活成功")

        # 读取夹爪位置
        status = gripper.OBJ()
        print(f"  当前夹爪状态: {status}")

        return True
    except ImportError as e:
        if "serial" in str(e):
            print("✗ pyserial 库未安装")
            print("  安装命令: pip install pyserial")
        else:
            print(f"✗ 导入失败: {e}")
        return False
    except Exception as e:
        print(f"✗ 夹爪连接失败: {e}")
        return False

def test_cameras():
    """测试 RealSense 相机"""
    print("\n=== 测试 RealSense 相机 ===")
    try:
        import pyrealsense2 as rs
        print("✓ pyrealsense2 库已安装")

        ctx = rs.context()
        devices = ctx.query_devices()

        if len(devices) == 0:
            print("✗ 未检测到 RealSense 设备")
            print("  请检查:")
            print("  1. RealSense 相机是否连接")
            print("  2. USB 3.0 连接（蓝色端口）")
            print("  3. 运行 lsusb | grep Intel")
            return False

        print(f"✓ 检测到 {len(devices)} 个 RealSense 设备")

        for i, device in enumerate(devices):
            print(f"\n  设备 {i+1}:")
            print(f"    名称: {device.get_info(rs.camera_info.name)}")
            print(f"    序列号: {device.get_info(rs.camera_info.serial_number)}")
            print(f"    固件版本: {device.get_info(rs.camera_info.firmware_version)}")

        print("\n提示: 请将上述序列号更新到 config_ur5e.py 的 cameras 配置中")

        return True
    except ImportError:
        print("✗ pyrealsense2 库未安装")
        print("  通常 lerobot 会自动安装此库")
        return False
    except Exception as e:
        print(f"✗ 相机检测失败: {e}")
        return False

def main():
    """主测试函数"""
    print("=" * 60)
    print("UR5e 硬件连接测试")
    print("=" * 60)

    results = []

    # 测试 RTDE
    results.append(("RTDE 连接", test_rtde()))

    # 测试夹爪
    results.append(("Robotiq 夹爪", test_gripper()))

    # 测试相机
    results.append(("RealSense 相机", test_cameras()))

    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)

    for name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{name:20s} {status}")

    all_passed = all(r for _, r in results)
    if all_passed:
        print("\n✓ 所有测试通过！可以运行 bash run_ur5e.sh")
        return 0
    else:
        print("\n✗ 部分测试失败，请根据上述提示修复问题")
        return 1

if __name__ == "__main__":
    sys.exit(main())
