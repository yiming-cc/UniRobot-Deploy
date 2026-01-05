import torch
from torch import Tensor, nn
import json_numpy
import requests
import numpy as np
from typing import Dict, Optional
from typing_extensions import Unpack
from lerobot.policies.pretrained import PreTrainedPolicy, ActionSelectKwargs
from .configuration_go1_client import GO1ClientConfig
from torch.nn import Linear

from .processor_go1_client import G1DataProcessor

from src.utils.visualize_utils import visualize_action_chunk_to_video
from src.utils.rotation_utils import RotationConverter
from scipy.spatial.transform import Rotation as R



class GO1ClientPolicy(PreTrainedPolicy):

    config_class = GO1ClientConfig
    name = "go1_client"
    
    
    def __init__(
        self,
        config: GO1ClientConfig,
    ):
        super().__init__(config)
        self.config = config
        if self.config.url is not None:
            self.url = f"{self.config.url}/act"
        else:
            self.url = f"http://{self.config.host}:{self.config.port}/act"
        self.reset()

        self.template_model = Linear(1, 1)

        self.processor = G1DataProcessor()

    def reset(self):
        self._cur_step: int = 0
        self._last_results = None
        
    @torch.no_grad()
    def select_action(self, batch: dict[str, Tensor]) -> Tensor:
        """Return action at each step.
        
        Args:
            batch: dict[str, Tensor]
        Returns:
            Tensor: action at each step
        """
        if self._last_results is None:
            payload = self.processor.forward_process(batch)
            action_chunk = self._post(payload)
            self._last_results = self.processor.backward_process(action_chunk)
            self._cur_step = 0

            # ---------------------------- debug visualize action chunk to video ----------------------------
            # obs_state = batch["observation.state"].cpu().numpy()

            # left_start_proprio = np.concatenate([obs_state[:, :3], RotationConverter.euler_to_quaternion(obs_state[:, 3:6])], axis=1)
            # left_all_action = np.concatenate([left_start_proprio, self._last_results[:, :7]], axis=0)
            # visualize_action_chunk_to_video(left_all_action, output_path="res/left_action_chunk_w_pro.mp4")
            # visualize_action_chunk_to_video(left_all_action[1:], output_path="res/left_action_chunk_wo_pro.mp4")

            # right_start_proprio = np.concatenate([obs_state[:, 7:10], RotationConverter.euler_to_quaternion(obs_state[:, 10:13])], axis=1)
            # right_all_action = np.concatenate([right_start_proprio, self._last_results[:, 8:15]], axis=0)
            # visualize_action_chunk_to_video(right_all_action, output_path="res/right_action_chunk_w_pro.mp4")
            # visualize_action_chunk_to_video(right_all_action[1:], output_path="res/right_action_chunk_wo_pro.mp4")
            # ---------------------------- debug visualize action chunk to video ----------------------------

        action = self._last_results[self._cur_step]
        action[14] = 1.0 if action[14] > 0.5 else 0.0
        action[29] = 1.0 if action[29] > 0.5 else 0.0

        self._cur_step += 1
        if self._cur_step >= self._last_results.shape[0]:
            self._last_results = None

        # Convert numpy array to torch.Tensor
        return torch.tensor(action, dtype=torch.float32)
            
    def _post(self, payload: Dict) -> np.ndarray:
        """Post observation to server and return action chunk.
        
        Args:
            payload: Dict
        Returns:
            np.ndarray: action chunk
        """
        try:
            resp = requests.post(self.url, json=payload)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            raise RuntimeError(f"Policy server request failed: {e}") from e

        action = np.array(data) # [T, 16]
        if action.ndim != 2:
            raise RuntimeError(f"Unexpected action shape from server: {action.shape}")
        return action


    def get_optim_params(self) -> dict:
        pass

    def forward(self, batch: dict[str, Tensor]) -> tuple[Tensor, dict | None]:
        pass

    def predict_action_chunk(self, batch: dict[str, Tensor], **kwargs: Unpack[ActionSelectKwargs]) -> Tensor:
        pass