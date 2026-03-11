import logging
import os
import time
from collections import deque
from threading import Event, Lock, Thread
from typing import Any, Optional

import cv2
import numpy as np
import websockets.sync.client
from openpi_client import msgpack_numpy
from openpi_client.websocket_client_policy import WebsocketClientPolicy

from ..bimanual_ur import BimanualUR

logger = logging.getLogger(__name__)


class StarVLAClient(WebsocketClientPolicy):
    """StarVLA client with integrated bimanual UR hardware control.

    Inherits WebsocketClientPolicy for WebSocket/msgpack transport,
    adds: observation, action execution, RTC async inference.
    Hardware init/lifecycle is managed by the BimanualUR instance.
    """

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: Optional[int] = None,
        robot: BimanualUR = None,
        execution_steps: int = 16,
        prefix_steps: int = 0,
        adaptive_prefix: bool = False,
        fps: int = 30,
        rtc: bool = False,
        action_type: str = "joint",
        verbose: bool = False,
        api_key: Optional[str] = None,
    ):
        # --- Hardware (managed externally) ---
        self.robot = robot
        self.action_type = action_type

        # --- WebSocket setup (parent handles connection + metadata) ---
        for k in ("HTTP_PROXY", "http_proxy", "HTTPS_PROXY", "https_proxy", "ALL_PROXY", "all_proxy"):
            os.environ.pop(k, None)
        host = host.replace("https://", "").replace("http://", "")
        host = f"ws://{host}"
        super().__init__(host=host, port=port, api_key=api_key)

        # --- Inference state ---
        self.task_description = None
        self.execution_steps = execution_steps
        self.max_prefix_steps = prefix_steps
        self.prefix_steps = prefix_steps
        self.adaptive_prefix = adaptive_prefix
        self.rtc = rtc
        self.fps = fps
        self.verbose = verbose
        self.action_queue = deque()

        if self.rtc:
            self.last_actions = None
            self.last_start_step = 0
            self.last_vla_input = None
            self.last_infer_elapsed = None
            self.last_delay = None
            self.worker_busy = False
            self._start_infer_async_thread()

    # ── WebSocket overrides ───────────────────────────────────────

    def _wait_for_server(self):
        """Override parent to add custom WebSocket params and timeout."""
        logging.info(f"Waiting for server at {self._uri}...")
        start_time = time.time()
        timeout = 600

        while True:
            if time.time() - start_time > timeout:
                raise TimeoutError(f"Failed to connect to server within {timeout}s")
            try:
                headers = {"Authorization": f"Api-Key {self._api_key}"} if self._api_key else None
                conn = websockets.sync.client.connect(
                    self._uri,
                    compression=None,
                    max_size=None,
                    additional_headers=headers,
                    open_timeout=150,
                    ping_interval=20,
                    ping_timeout=60,
                )
                metadata = msgpack_numpy.unpackb(conn.recv())
                logging.info(f"Connected to server at {self._uri}")
                return conn, metadata
            except ConnectionRefusedError:
                logging.info(f"Still waiting for server {self._uri} ...")
                time.sleep(2)

    def infer(self, obs: dict) -> dict:
        """Override parent to wrap StarVLA protocol format with retry."""
        query_info = {"payload": obs, "type": "infer"}
        data = self._packer.pack(query_info)
        for attempt in range(3):
            try:
                self._ws.send(data)
                response = self._ws.recv()
                if isinstance(response, str):
                    raise RuntimeError(f"Error in inference server:\n{response}")
                return msgpack_numpy.unpackb(response)
            except RuntimeError:
                raise
            except Exception as e:
                logging.warning(f"infer attempt {attempt + 1} failed: {e}")
                if attempt < 2:
                    self._reconnect()
                else:
                    raise

    def _reconnect(self):
        logging.warning(f"WebSocket connection lost, reconnecting to {self._uri} ...")
        try:
            self._ws.close()
        except Exception:
            pass
        self._ws, self._server_metadata = self._wait_for_server()
        logging.info("Reconnected successfully.")

    # ── Observation & Action (hardware-specific for this model) ───

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

    # ── Data formatting ───────────────────────────────────────────

    @staticmethod
    def encode_image(img: np.ndarray, quality: int = 70) -> bytes:
        _, buf = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        return buf.tobytes()

    @staticmethod
    def _extract_actions(response: dict) -> np.ndarray:
        if response.get("status") == "error" or not response.get("ok", True):
            error_msg = response.get("error", {})
            if isinstance(error_msg, dict):
                error_msg = error_msg.get("message", str(error_msg))
            raise RuntimeError(f"Server inference error: {error_msg}")
        return response["data"]["actions"][0]

    # ── Action queue: sync mode ───────────────────────────────────

    def _infer_sync(self, vla_input: dict):
        if len(self.action_queue) == 0:
            start_time = time.time()
            response = self.infer(vla_input)
            elapsed = time.time() - start_time
            if self.verbose:
                print(f"Infer elapsed: {int(elapsed * 1000)}ms")
            actions = self._extract_actions(response)
            self.action_queue.clear()
            for i in range(min(self.execution_steps, actions.shape[0])):
                self.action_queue.append((actions[i], i))

    # ── Action queue: RTC async mode ─────────────────────────────

    def _start_infer_async_thread(self):
        self.stop_event = Event()
        self.lock = Lock()
        self.thread = Thread(target=self._run_infer_async_loop, daemon=True)
        self.thread.start()

    def _run_infer_async_loop(self):
        while not self.stop_event.is_set():
            vla_input = None
            with self.lock:
                if self.last_vla_input is not None and not self.worker_busy:
                    vla_input = self.last_vla_input
                    self.last_vla_input = None
                    self.worker_busy = True
            if vla_input is None:
                time.sleep(0.001)
                continue

            start_time = time.time()
            with self.lock:
                remain_steps = len(self.action_queue)
                self.last_delay = min(remain_steps, self.prefix_steps)
                delay = self.last_delay
                if delay > 0:
                    start_step = self.action_queue[0][1]
                    actions_prefix = np.array([self.action_queue[i][0] for i in range(delay)])
                else:
                    start_step = 0
                    actions_prefix = None

            if actions_prefix is not None:
                vla_input["actions"] = [actions_prefix]
            vla_input["delay"] = delay
            actions = self._extract_actions(self.infer(vla_input))
            elapsed = time.time() - start_time

            with self.lock:
                self.last_actions = actions
                self.last_start_step = start_step
                self.last_vla_input = None
                if self.adaptive_prefix:
                    self.prefix_steps = min(self.max_prefix_steps, int(elapsed * self.fps) + 1)
                    if self.verbose:
                        print(f"Infer RTC elapsed: {int(elapsed * 1000)}ms, prefix_steps adapted to {self.prefix_steps}")
                elif self.verbose:
                    print(f"Infer RTC elapsed: {int(elapsed * 1000)}ms")
                self.worker_busy = False

    def _check_actions(self):
        last_actions = None
        last_delay = None
        last_start_step = None
        with self.lock:
            if self.last_actions is not None:
                last_actions = self.last_actions.copy()
                last_delay = self.last_delay
                last_start_step = self.last_start_step
                self.last_actions = None
        if last_actions is not None:
            if last_delay is not None:
                last_actions = last_actions[last_delay:]
            start_step = last_start_step + last_delay
            while len(self.action_queue) > 0 and self.action_queue[-1][1] > start_step:
                self.action_queue.pop()
            for i in range(min(self.execution_steps, last_actions.shape[0])):
                self.action_queue.append((last_actions[i], start_step + i))

    def _infer_async(self, vla_input: dict):
        self._check_actions()
        if len(self.action_queue) == self.prefix_steps or len(self.action_queue) == 0:
            with self.lock:
                self.last_vla_input = vla_input.copy()
        while len(self.action_queue) == 0:
            self._check_actions()

    # ── Public API ────────────────────────────────────────────────

    def reset(self, task_description: str = None):
        if task_description is not None:
            self.task_description = task_description
        self.action_queue.clear()
        if self.rtc:
            with self.lock:
                while self.worker_busy:
                    time.sleep(0.01)
            self.last_actions = None
            self.last_start_step = 0
            self.last_vla_input = None
            self.last_infer_elapsed = None
            self.last_delay = None
            self.worker_busy = False

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
        camera_names = list(self.robot.config.camera_serial_numbers.keys())
        images = [obs[cam] for cam in camera_names]
        state = np.concatenate([obs["ee_pos_rot"], obs["joint_positions"]])[None]  # (1, D)

        # 2. Build VLA input
        vla_input = {}
        vla_input["batch_images"] = [[self.encode_image(img) for img in images]]
        if self.task_description is not None:
            vla_input["instructions"] = [self.task_description]
        vla_input["state"] = [state]
        if fps is not None:
            vla_input["fps"] = [fps]
        if view_mask is not None:
            vla_input["view_mask"] = [view_mask]

        # 3. Infer (sync or RTC)
        start = time.perf_counter()
        if self.rtc:
            self._infer_async(vla_input)
        else:
            self._infer_sync(vla_input)
        elapsed_ms = (time.perf_counter() - start) * 1000
        if elapsed_ms > 1 and self.verbose:
            print(f"Step elapsed: {elapsed_ms:.0f}ms")

        action_values = self.action_queue.popleft()[0]

        # 4. Execute action on hardware
        action_dict = {}
        for i in range(14):
            action_dict[f"ee_pos_rot_{i}"] = action_values[i].item()
        for i in range(14):
            action_dict[f"joint_positions_{i}"] = action_values[14 + i].item()
        self.send_action(action_dict, action_type=action_type or self.action_type)

        return action_values

    def close(self):
        if hasattr(self, "stop_event"):
            self.stop_event.set()
        if hasattr(self, "thread"):
            self.thread.join()
        try:
            self._ws.close()
        except Exception:
            pass


