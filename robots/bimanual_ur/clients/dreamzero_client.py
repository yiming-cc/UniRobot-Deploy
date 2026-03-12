import logging
import os
import time
import uuid
from collections import deque
from typing import Any, Optional

import cv2
import numpy as np
import websockets.sync.client
from openpi_client import msgpack_numpy

from ..bimanual_ur import BimanualUR

logger = logging.getLogger(__name__)

# DreamZero protocol constants
ACTION_HORIZON = 24          # Server returns 24-step action chunks
IMAGE_WIDTH = 320
IMAGE_HEIGHT = 180
FRAME_INDICES = [0, 7, 15, 23]  # 4-frame selection from 24-frame buffer


class DreamZeroClient:
    """DreamZero client with integrated bimanual UR hardware control.

    Directly manages WebSocket + msgpack transport (no WebsocketClientPolicy).
    Implements multi-frame buffering: first inference sends 1 frame, subsequent
    inferences send 4 frames selected from a 24-frame rolling buffer.
    """

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
        # --- Hardware ---
        self.robot = robot
        self.action_type = action_type

        # --- Inference state ---
        self.task_description = None
        self.fps = fps
        self.verbose = verbose
        self.action_queue: deque[np.ndarray] = deque()

        # --- Session ---
        self._session_id = str(uuid.uuid4())
        self._is_first_inference = True
        self._global_step = 0

        # --- Frame buffers (one deque per camera) ---
        camera_names = list(self.robot.config.camera_serial_numbers.keys())
        self._frame_buffer: dict[str, deque] = {
            name: deque(maxlen=ACTION_HORIZON) for name in camera_names
        }

        # --- WebSocket setup ---
        for k in ("HTTP_PROXY", "http_proxy", "HTTPS_PROXY", "https_proxy", "ALL_PROXY", "all_proxy"):
            os.environ.pop(k, None)

        # Build URI: https:// → wss://, http:// → ws://, bare host → ws://
        if host.startswith("https://"):
            host = "wss://" + host[len("https://"):]
        elif host.startswith("http://"):
            host = "ws://" + host[len("http://"):]
        elif not host.startswith("ws://") and not host.startswith("wss://"):
            host = f"ws://{host}"
        if port is not None and f":{port}" not in host:
            self._uri = f"{host}:{port}"
        else:
            self._uri = host

        self._api_key = api_key
        self._packer = msgpack_numpy.Packer()
        self._ws, self._server_metadata = self._connect()
        logger.info(f"Connected to DreamZero server at {self._uri}")
        if self.verbose:
            logger.info(f"Server metadata: {self._server_metadata}")

    # ── WebSocket transport ────────────────────────────────────────

    def _connect(self):
        """Connect to DreamZero server with generous timeout for model warmup."""
        logger.info(f"Connecting to DreamZero server at {self._uri} ...")
        start_time = time.time()
        timeout = 600

        while True:
            if time.time() - start_time > timeout:
                raise TimeoutError(f"Failed to connect to server within {timeout}s")
            try:
                headers = {"Authorization": f"Api-Key {self._api_key}"} if self._api_key else None
                ws = websockets.sync.client.connect(
                    self._uri,
                    compression=None,
                    max_size=None,
                    additional_headers=headers,
                    open_timeout=150,
                    ping_interval=60,
                    ping_timeout=600,
                )
                metadata = msgpack_numpy.unpackb(ws.recv())
                return ws, metadata
            except ConnectionRefusedError:
                logger.info(f"Still waiting for server {self._uri} ...")
                time.sleep(2)

    def _reconnect(self):
        logger.warning(f"WebSocket connection lost, reconnecting to {self._uri} ...")
        try:
            self._ws.close()
        except Exception:
            pass
        self._ws, self._server_metadata = self._connect()
        logger.info("Reconnected successfully.")

    def _infer_ws(self, obs: dict) -> np.ndarray:
        """Send observation to server and receive action array."""
        obs["endpoint"] = "infer"
        data = self._packer.pack(obs)
        for attempt in range(3):
            try:
                self._ws.send(data)
                response = self._ws.recv()
                if isinstance(response, str):
                    raise RuntimeError(f"Error from DreamZero server:\n{response}")
                return msgpack_numpy.unpackb(response)
            except RuntimeError:
                raise
            except Exception as e:
                logger.warning(f"infer attempt {attempt + 1} failed: {e}")
                if attempt < 2:
                    self._reconnect()
                else:
                    raise

    def _reset_ws(self, info: dict):
        """Notify server to reset session (save video, clear state)."""
        info["endpoint"] = "reset"
        data = self._packer.pack(info)
        try:
            self._ws.send(data)
            self._ws.recv()
        except Exception as e:
            logger.warning(f"reset notification failed: {e}")

    # ── Observation ────────────────────────────────────────────────

    def get_observation(self, use_camera=True) -> dict[str, Any]:
        obs_dict = {}
        if use_camera:
            for key, cam in self.robot.cameras.items():
                obs_dict[key] = cam.read()

        obs_dict["left_joint_positions"] = self.robot.left_arm.get_joint_state()
        obs_dict["right_joint_positions"] = self.robot.right_arm.get_joint_state()
        obs_dict["left_ee_pos_rot"] = self.robot.left_arm.get_tcp_state()
        obs_dict["right_ee_pos_rot"] = self.robot.right_arm.get_tcp_state()

        return obs_dict

    # ── Frame buffer & multi-frame dispatch ────────────────────────

    def _buffer_frames(self, obs: dict):
        """Resize camera images to (180, 320) and append to frame buffers."""
        for cam_name in self._frame_buffer:
            img = obs[cam_name]
            resized = cv2.resize(img, (IMAGE_WIDTH, IMAGE_HEIGHT))
            self._frame_buffer[cam_name].append(resized)

    def _get_frames(self, cam_name: str) -> np.ndarray:
        """Get frames for inference: 1 frame (first call) or 4 frames (subsequent)."""
        buf = self._frame_buffer[cam_name]

        if self._is_first_inference:
            # First inference: single frame (H, W, 3)
            return buf[-1]
        else:
            # Subsequent: 4 frames from indices [0, 7, 15, 23] in the 24-frame buffer
            frames = [buf[i] for i in FRAME_INDICES]
            return np.stack(frames, axis=0)  # (4, H, W, 3)

    def _build_observation(self, obs: dict) -> dict:
        """Build DreamZero-format observation dict."""
        dz_obs = {}

        # Images: single frame or 4 frames per camera
        for cam_name in self._frame_buffer:
            dz_obs[f"observation/{cam_name}"] = self._get_frames(cam_name)

        # Robot state: 4 separate keys, each (7,)
        dz_obs["observation/left_joint_positions"] = obs["left_joint_positions"]
        dz_obs["observation/right_joint_positions"] = obs["right_joint_positions"]
        dz_obs["observation/left_ee_pos_rot"] = obs["left_ee_pos_rot"]
        dz_obs["observation/right_ee_pos_rot"] = obs["right_ee_pos_rot"]

        # Task prompt
        if self.task_description is not None:
            dz_obs["prompt"] = self.task_description

        # Session ID
        dz_obs["session_id"] = self._session_id

        return dz_obs

    # ── Action parsing & execution ─────────────────────────────────

    def send_action(self, action: np.ndarray, action_type: Optional[str] = None) -> None:
        """Execute a single 28-dim action on hardware.

        Action layout (28D):
          [0:7]   left_joint_positions   (6 joints + gripper)
          [7:14]  right_joint_positions  (6 joints + gripper)
          [14:21] left_ee_pos_rot        (6D pose + gripper)
          [21:28] right_ee_pos_rot       (6D pose + gripper)
        """
        action_type = action_type or self.action_type
        if action_type in ("joint", "gello"):
            self.robot.left_arm.step_joint(action[0:7])
            self.robot.right_arm.step_joint(action[7:14])
        elif action_type == "tcp":
            self.robot.left_arm.step_tcp(action[14:21])
            self.robot.right_arm.step_tcp(action[21:28])
        else:
            raise ValueError(f"Unknown action_type: {action_type}")

    # ── Public API ────────────────────────────────────────────────

    def reset(self, task_description: str = None):
        """Reset session: new UUID, clear buffers, notify server."""
        if task_description is not None:
            self.task_description = task_description

        self._session_id = str(uuid.uuid4())
        self.action_queue.clear()
        for buf in self._frame_buffer.values():
            buf.clear()
        self._global_step = 0
        self._is_first_inference = True

        self._reset_ws({"session_id": self._session_id})
        logger.info(f"Session reset, new session_id: {self._session_id}")

    def step(
        self,
        task_description: Optional[str] = None,
        fps: Optional[int] = None,
        action_type: Optional[str] = None,
        view_mask=None,
    ) -> np.ndarray:
        """Single-frame step: observe -> buffer -> infer (if needed) -> execute."""
        # Task change triggers reset
        if task_description is not None and task_description != self.task_description:
            self.reset(task_description)

        # 1. Observe
        obs = self.get_observation()

        # 2. Buffer camera frames (resize to 180x320)
        self._buffer_frames(obs)

        # 3. Infer when action queue is empty
        if len(self.action_queue) == 0:
            dz_obs = self._build_observation(obs)

            start = time.perf_counter()
            actions = self._infer_ws(dz_obs)  # (24, 28)
            elapsed_ms = (time.perf_counter() - start) * 1000

            if self.verbose:
                logger.info(
                    f"Inference: {elapsed_ms:.0f}ms, "
                    f"actions shape={actions.shape}, "
                    f"frames={'1' if self._is_first_inference else '4'}, "
                    f"step={self._global_step}"
                )

            # Enqueue all 24 actions
            for i in range(actions.shape[0]):
                self.action_queue.append(actions[i])

            self._is_first_inference = False

        # 4. Dequeue and execute
        action = self.action_queue.popleft()
        self.send_action(action, action_type=action_type or self.action_type)

        self._global_step += 1
        return action

    def close(self):
        """Clean up: notify server reset and close WebSocket."""
        try:
            self._reset_ws({"session_id": self._session_id})
        except Exception:
            pass
        try:
            self._ws.close()
        except Exception:
            pass
