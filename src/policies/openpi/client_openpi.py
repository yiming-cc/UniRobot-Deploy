import math
import os
import re
from collections import deque

import safetensors
import torch
import torch.nn.functional as F  # noqa: N812
from torch import Tensor, nn
from transformers import AutoProcessor

from lerobot.constants import ACTION, OBS_STATE
from lerobot.policies.normalize import (
    Normalize,
    Unnormalize,
)
from dataclasses import dataclass, field

from lerobot.configs.policies import PreTrainedConfig
from lerobot.configs.types import FeatureType, NormalizationMode, PolicyFeature
from lerobot.optim.optimizers import AdamWConfig
from lerobot.optim.schedulers import (
    CosineDecayWithWarmupSchedulerConfig,
)

from openpi_client import image_tools
from openpi_client import websocket_client_policy
import numpy as np
import time

@dataclass
class PiClientConfig:
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    host: str = "localhost"
    port: int = 8000

class PiClientPolicy:
    """Wrapper class around VLAFlowMatching model to train and run inference within LeRobot."""

    config_class = PiClientConfig
    name = "smolvla"
    def __init__(self, host, action_horizon=5):
        self.config = PiClientConfig(host=host)
        self.client = websocket_client_policy.WebsocketClientPolicy(host=self.config.host, port=self.config.port)
        self._cur_step: int = 0
        self._last_results = None
        self._action_horizon = action_horizon
        self.start_state = None

    def reset(self):
        self._cur_step: int = 0
        self._last_results = None
    
    @torch.no_grad()
    def select_action(self, batch: dict[str, Tensor], noise: Tensor | None = None) -> Tensor:
        if self._last_results is None:
            inputs = {}
            inputs["observation/state"] = batch["observation.state"].cpu().numpy()[0]
            inputs["observation/images/front"] = batch["observation.images.front"][0].permute(1, 2, 0).cpu().numpy()
            inputs["prompt"] = batch["task"]
            self._last_results = self.client.infer(inputs)["actions"]
            self.delta_action = self._last_results - batch["observation.state"].cpu().numpy()[:,:7]
            np.set_printoptions(suppress=True, precision=3)  
            print(self._last_results)
            # self.delta_action[..., :6] = np.clip(self.delta_action[..., :6], -0.3, 0.3)
            # self.delta_action[..., :6] = np.clip(self.delta_action[..., :6], -0.2, 0.2)
            # self.delta_action[..., :3] = np.clip(self.delta_action[..., :3], -0.1, 0.1)
            # breakpoint()
            self.delta_action_delta = np.concatenate([self.delta_action[1:], self.delta_action[-1:]]) - self.delta_action
            # self.delta_action_delta[:, 3:6] = np.clip(self.delta_action_delta[:, 3:6], -0.02, 0.02)
            
            self.delta_action_delta[:, 3:6] = np.clip(self.delta_action_delta[:, 3:6], -0.02, 0.02)
            # self.delta_action_delta[:, 0:6] = np.clip(self.delta_action_delta[:, 0:6], -0.02, 0.02)
            
            # self.delta_action_delta[:, 3:6] = np.clip(self.delta_action_delta[:, 3:6], -0.2, 0.2)
            # self.delta_action_delta = np.clip(self.delta_action_delta, -0.05, 0.05)
            self.delta_action[:, :6] = np.cumsum(self.delta_action_delta[:, :6], axis=0)
            # self.delta_action[..., 3:6] = np.clip(self.delta_action[..., 3:6], -0.1, 0.1)
            
            self._last_results = self.delta_action + batch["observation.state"].cpu().numpy()[:,:7]
            # self._last_results = self.delta_action
            # self._last_results[..., :6] = self._last_results[..., :6] + batch["observation.state"].cpu().numpy()[:,:6]
        
            self._last_results[..., 6] = self._last_results[..., 6] > 0.1
            # self._last_results[..., 6] = self._last_results[..., 6] > 0.3
            # self._last_results[..., 6] = self._last_results[..., 6] > 0.8
            
            
            # self._last_results = batch["observation.state"].cpu().numpy()[:,:7].repeat(self._action_horizon, axis=0)
            self._cur_step = 0
            # import pdb;pdb.set_trace()
        
        action = self._last_results[self._cur_step]
        # delta_action = self.delta_action[self._cur_step, :].tolist()
        # print(f"Step {self._cur_step}/{self._action_horizon}, delta: {delta_action[0]:.4f}, {delta_action[1]:.4f}, {delta_action[2]:.4f}, {delta_action[3]:.4f}, {delta_action[4]:.4f}, {delta_action[5]:.4f}, {delta_action[6]:.4f}")
        # action = batch["observation.state"].cpu().numpy()[0]
        # action = action + np.random.randn(*action.shape) * 0.01
        self._cur_step += 1

        if self._cur_step >= self._action_horizon:
            self._last_results = None
        # time.sleep(0.1)
        return torch.from_numpy(action).float()