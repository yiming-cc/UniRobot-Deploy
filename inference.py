#!/usr/bin/env python
"""Minimal inference loop: client.step() handles observe → infer → execute."""

import argparse
import time
import logging

import numpy as np

from robots import CLIENT_REGISTRY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def busy_wait(duration: float):
    end = time.perf_counter() + duration
    while time.perf_counter() < end:
        pass


def main():
    # Two-pass parsing: first get --client, then add client-specific args
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--client", type=str, default="bimanual_ur_starvla",
                            choices=list(CLIENT_REGISTRY.keys()),
                            help=f"Client type: {', '.join(CLIENT_REGISTRY.keys())}")
    pre_args, _ = pre_parser.parse_known_args()

    parser = argparse.ArgumentParser(description="UniRobot inference", parents=[pre_parser])
    parser.add_argument("--host", type=str, required=True, help="Server host URL")
    parser.add_argument("--port", type=int, default=None, help="Server port (if not in URL)")
    parser.add_argument("--task", type=str, required=True, help="Task description")
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--debug", action="store_true", help="Mock robot hardware for testing")

    # Add client-specific arguments
    entry = CLIENT_REGISTRY[pre_args.client]
    if entry.add_arguments:
        entry.add_arguments(parser)

    args = parser.parse_args()

    if args.debug:
        client = MockStarVLAClient()
        client.connect()
        robot = None
    else:
        robot, client = entry.factory(args)

    print(f"Starting inference loop: client='{args.client}', task='{args.task}', fps={args.fps}")

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
                # print(f"Loop: {total * 1000:.1f}ms ({1.0 / total:.1f} Hz)")

    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        client.close()
        if robot is not None:
            robot.disconnect()
        print("Disconnected.")


class MockStarVLAClient:
    """Mock client for testing without hardware or server."""

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
