#!/usr/bin/env python
"""Minimal inference loop: client.step() handles observe → infer → execute."""

import argparse
import time
import logging

import numpy as np

from robots.bimanual_ur import BimanualURConfig, BimanualUR
from robots.bimanual_ur.clients.starvla_client import StarVLAClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def busy_wait(duration: float):
    end = time.perf_counter() + duration
    while time.perf_counter() < end:
        pass


def main():
    parser = argparse.ArgumentParser(description="StarVLA bimanual UR inference")
    parser.add_argument("--host", type=str, required=True, help="StarVLA server host URL")
    parser.add_argument("--port", type=int, default=None, help="Server port (if not in URL)")
    parser.add_argument("--task", type=str, required=True, help="Task description")
    parser.add_argument("--action_type", type=str, default="joint", choices=["joint", "tcp"])
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--execution_steps", type=int, default=16)
    parser.add_argument("--prefix_steps", type=int, default=8)
    parser.add_argument("--rtc", action="store_true", default=True, help="Enable RTC async mode")
    parser.add_argument("--no-rtc", dest="rtc", action="store_false")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--debug", action="store_true", help="Mock robot hardware for testing")
    args = parser.parse_args()

    config = BimanualURConfig()

    if args.debug:
        client = MockStarVLAClient(config)
        client.connect()
    else:
        robot = BimanualUR(config)
        robot.connect()
        client = StarVLAClient(
            host=args.host,
            port=args.port,
            robot=robot,
            execution_steps=args.execution_steps,
            prefix_steps=args.prefix_steps,
            fps=args.fps,
            rtc=args.rtc,
            action_type=args.action_type,
            verbose=args.verbose,
        )

    camera_names = list(config.camera_serial_numbers.keys())
    print(f"Starting inference loop: task='{args.task}', fps={args.fps}, action_type={args.action_type}")
    print(f"Cameras: {camera_names}")
    print(f"RTC: {args.rtc}, execution_steps={args.execution_steps}, prefix_steps={args.prefix_steps}")

    try:
        while True:
            loop_start = time.perf_counter()

            client.step(task_description=args.task, fps=args.fps)

            elapsed = time.perf_counter() - loop_start
            remaining = 1.0 / args.fps - elapsed
            if remaining > 0:
                busy_wait(remaining)

            if args.verbose:
                total = time.perf_counter() - loop_start
                print(f"Loop: {total * 1000:.1f}ms ({1.0 / total:.1f} Hz)")

    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        client.close()
        if not args.debug:
            robot.disconnect()
        print("Disconnected.")


class MockStarVLAClient:
    """Mock client for testing without hardware or server."""

    def __init__(self, config):
        self.config = config
        self.camera_names = list(config.camera_serial_numbers.keys())

    def connect(self):
        print("[Mock] Client connected")

    def step(self, task_description=None, fps=None, action_type=None, view_mask=None):  # noqa: ARG002
        _ = task_description, fps, action_type, view_mask
        return np.zeros(28)

    def close(self):
        print("[Mock] Client disconnected")

    def go_home(self):
        pass


if __name__ == "__main__":
    main()
