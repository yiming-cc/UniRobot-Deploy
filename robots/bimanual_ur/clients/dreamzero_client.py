import logging
import time
from collections import deque
from typing import Any, Optional

import numpy as np
from openpi_client import image_tools
from openpi_client.websocket_client_policy import WebsocketClientPolicy

from ..bimanual_ur import BimanualUR

logger = logging.getLogger(__name__)


class DreamZeroClient(WebsocketClientPolicy):
    """DreamZero client with integrated bimanual UR hardware control.

    Uses standard openpi WebSocket protocol (no custom wrapping).
    No RTC mode — simple sync inference with action chunk caching.
    """

    # Default image size for openpi models.
    IMAGE_SIZE = 224

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: Optional[int] = None,
        robot: BimanualUR = None,
        fps: int = 30,
        action_type: str = "joint",
        verbose: bool = False,
        api_key: Optional[str] = None,
    ):
        # --- Hardware (managed externally) ---
        self.robot = robot
        self.action_type = action_type

        # --- WebSocket setup (parent handles connection + metadata) ---
        super().__init__(host=host, port=port, api_key=api_key)

        # --- Inference state ---
        self.task_description = None
        self.fps = fps
        self.verbose = verbose
        self.action_queue = deque()

    # ── Observation & Action (same hardware as StarVLA) ────────────

    def get_observation(self, use_camera=True) -> dict[str, Any]:
        obs_dict = {}
        if use_camera:
            for key, cam in self.robot.cameras.items():
                obs_dict[key] = cam.read()

        left_tcp = self.robot.left_arm.get_tcp_state()
        right_tcp = self.robot.right_arm.get_tcp_state()
        left_joints = self.robot.left_arm.get_joint_state()
        right_joints = self.robot.right_arm.get_joint_state()

        obs_dict["ee_pos_rot"] = np.concatenate([left_tcp, right_tcp])
        obs_dict["joint_positions"] = np.concatenate([left_joints, right_joints])

        return obs_dict

    def send_action(self, action: dict, action_type: Optional[str] = None) -> None:
        action_type = action_type or self.action_type
        if action_type in ("joint", "gello"):
            joint_action = np.array([action[f"joint_positions_{i}"] for i in range(14)])
            self.robot.left_arm.step_joint(joint_action[:7])
            self.robot.right_arm.step_joint(joint_action[7:])
        elif action_type == "tcp":
            tcp_action = np.array([action[f"ee_pos_rot_{i}"] for i in range(14)])
            self.robot.left_arm.step_tcp(tcp_action[:7])
            self.robot.right_arm.step_tcp(tcp_action[7:])
        else:
            raise ValueError(f"Unknown action_type: {action_type}")

    # ── Data formatting (standard openpi protocol) ────────────────

    @staticmethod
    def _prepare_image(img: np.ndarray, size: int = 224) -> np.ndarray:
        """Resize and convert image for openpi server."""
        return image_tools.convert_to_uint8(
            image_tools.resize_with_pad(img, size, size)
        )

    def _build_observation(self, obs: dict) -> dict:
        """Build openpi-format observation dict from raw observation."""
        openpi_obs = {}

        # Images: observation/<camera_name>
        camera_names = list(self.robot.config.camera_serial_numbers.keys())
        for cam_name in camera_names:
            img = self._prepare_image(obs[cam_name], self.IMAGE_SIZE)
            openpi_obs[f"observation/{cam_name}"] = img

        # State: concatenated TCP + joint positions
        state = np.concatenate([obs["ee_pos_rot"], obs["joint_positions"]])
        openpi_obs["observation/state"] = state

        # Task prompt
        if self.task_description is not None:
            openpi_obs["prompt"] = self.task_description

        return openpi_obs

    # ── Sync inference with action chunk caching ──────────────────

    def _infer_sync(self, openpi_obs: dict):
        """Fetch new action chunk from server when queue is empty."""
        if len(self.action_queue) == 0:
            start_time = time.time()
            response = self.infer(openpi_obs)
            elapsed = time.time() - start_time
            if self.verbose:
                print(f"Infer elapsed: {int(elapsed * 1000)}ms")

            actions = response["actions"]  # (action_horizon, action_dim)
            for i in range(actions.shape[0]):
                self.action_queue.append(actions[i])

    # ── Public API ────────────────────────────────────────────────

    def reset(self, task_description: str = None):
        if task_description is not None:
            self.task_description = task_description
        self.action_queue.clear()

    def step(
        self,
        task_description: Optional[str] = None,
        fps: Optional[int] = None,
        action_type: Optional[str] = None,
        view_mask=None,
    ) -> np.ndarray:
        """Single-frame step: observe → infer → execute. Returns raw action array."""
        if task_description is not None and task_description != self.task_description:
            self.reset(task_description)

        # 1. Observe
        obs = self.get_observation()

        # 2. Build openpi observation
        openpi_obs = self._build_observation(obs)

        # 3. Infer (sync only, with action chunk caching)
        start = time.perf_counter()
        self._infer_sync(openpi_obs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        if elapsed_ms > 1 and self.verbose:
            print(f"Step elapsed: {elapsed_ms:.0f}ms")

        action_values = self.action_queue.popleft()

        # 4. Execute action on hardware
        action_dict = {}
        for i in range(14):
            action_dict[f"ee_pos_rot_{i}"] = action_values[i].item()
        for i in range(14):
            action_dict[f"joint_positions_{i}"] = action_values[14 + i].item()
        self.send_action(action_dict, action_type=action_type or self.action_type)

        return action_values

    def close(self):
        try:
            self._ws.close()
        except Exception:
            pass
