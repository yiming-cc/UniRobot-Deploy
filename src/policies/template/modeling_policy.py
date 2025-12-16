import torch
from torch import Tensor, nn
import json_numpy
import requests
import numpy as np
from typing import Dict, Optional
from typing_extensions import Unpack
from lerobot.policies.pretrained import PreTrainedPolicy, ActionSelectKwargs
from .configuration_policy import PolicyTemplateConfig
from torch.nn import Linear





class PolicyTemplatePolicy(PreTrainedPolicy):

    config_class = PolicyTemplateConfig
    name = "xvla_client"
    
    
    def __init__(
        self,
        config: PolicyTemplateConfig,
    ):
        super().__init__(config)
        self.config = config
        pass

    def reset(self):
        pass
        
    @torch.no_grad()
    def select_action(self, batch: dict[str, Tensor]) -> Tensor:
        """Return action at each step.
        
        Args:
            batch: dict[str, Tensor]
        Returns:
            Tensor: action at each step
        """
        pass

    def get_optim_params(self) -> dict:
        pass

    def forward(self, batch: dict[str, Tensor]) -> tuple[Tensor, dict | None]:
        pass

    def predict_action_chunk(self, batch: dict[str, Tensor], **kwargs: Unpack[ActionSelectKwargs]) -> Tensor:
        pass