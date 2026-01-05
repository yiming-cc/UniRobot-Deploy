from lerobot.processor import (
    PolicyProcessorPipeline,
    PolicyAction,
    ProcessorStep,
)
from lerobot.processor.converters import (
    policy_action_to_transition,
    transition_to_policy_action,
)

from dataclasses import dataclass
from typing import Any, List, Dict

import numpy as np
import torch

from .configuration_xvla_client import XVLAClientConfig

import json_numpy
from src.utils.rotation_utils import RotationConverter


EPS = 1e-6


def make_xvla_client_pre_post_processors(
    config: XVLAClientConfig,
    dataset_stats: dict[str, dict[str, torch.Tensor]] | None = None,
) -> tuple[
    PolicyProcessorPipeline[dict[str, Any], dict[str, Any]],
    PolicyProcessorPipeline[PolicyAction, PolicyAction],
]:
    pre_processor_steps: list[ProcessorStep] = []
    post_processor_steps: list[ProcessorStep] = []


    return (
        PolicyProcessorPipeline[dict[str, Any], dict[str, Any]](
            steps=pre_processor_steps,
        ),
        PolicyProcessorPipeline[PolicyAction, PolicyAction](
            steps=post_processor_steps,
            to_transition=policy_action_to_transition,
            to_output=transition_to_policy_action,
        ),
    )

class G1DataProcessor:

    def __init__(self):
        pass

    def forward_process(self, batch: dict[str, Any]) -> Dict:
        """convert G1 batch data to XVLA client input data
        """

        main_view = (batch["observation.images.head"][0].permute(1, 2, 0).cpu().numpy()* 255).astype(np.uint8)
        
        hand_left = (batch["observation.images.hand_left"][0].permute(1, 2, 0).cpu().numpy()* 255).astype(np.uint8)
        hand_right = (batch["observation.images.hand_right"][0].permute(1, 2, 0).cpu().numpy()* 255).astype(np.uint8)

        proprio = np.zeros(20) # [..., (pos+rot6d+gripper)*2]
        observation_state = batch["observation.state"][0].cpu().numpy() # [..., (pos+euler+gripper)*2]

        # for i in range(2):
        #     # position
        #     proprio[i*10:i*10+3] = observation_state[i*7:i*7+3]
        #     # rotation
        #     proprio[i*10+3:i*10+9] = RotationConverter.euler_to_rotate6d(observation_state[i*7+3:i*7+6], row_concat=True)
        #     # gripper
        #     proprio[i*10+9] = observation_state[i*7+6]

        # position
        proprio[0:3] = observation_state[0:3]
        proprio[10:13] = observation_state[14:17]

        # rotation
        proprio[3:9] = RotationConverter.euler_to_rotate6d(observation_state[3:6], row_concat=True)
        proprio[13:19] = RotationConverter.euler_to_rotate6d(observation_state[17:20], row_concat=True)

        # gripper
        proprio[9] = observation_state[13]
        proprio[19] = observation_state[27]


        return {
            "proprio": json_numpy.dumps(proprio),
            "language_instruction": batch["task"],
            "image0": json_numpy.dumps(main_view),
            "image1": json_numpy.dumps(hand_left),
            "image2": json_numpy.dumps(hand_right),
            "domain_id": 15,
            "steps": 10,
        }

    def backward_process(self, action_chunk: np.ndarray) -> np.ndarray:
        """convert action chunk from xvla action chunk to g1 action features

        Args:
            action_chunk: [..., 20] # [..., (pos+rot6d+gripper)*2]
        Returns:
            processed_action_chunk: [..., 31]
        """

        processed_action_chunk = np.zeros((action_chunk.shape[0], 31))

        # for i in range(2):
        #     # position
        #     processed_action_chunk[:, i*8:i*8+3] = action_chunk[:, i*10:i*10+3]
        #     # rotation
        #     processed_action_chunk[:, i*8+3:i*8+7] = RotationConverter.rotate6d_to_quaternion(action_chunk[:, i*10+3:i*10+9], row_concat=True)
        #     # gripper
        #     processed_action_chunk[:, i*8+7] = action_chunk[:, i*10+9]

        # position
        processed_action_chunk[:, 0:3] = action_chunk[:, 0:3]
        processed_action_chunk[:, 15:18] = action_chunk[:, 10:13]

        # rotation
        processed_action_chunk[:, 3:7] = RotationConverter.rotate6d_to_quaternion(action_chunk[:, 3:9], row_concat=True)
        processed_action_chunk[:, 18:22] = RotationConverter.rotate6d_to_quaternion(action_chunk[:, 13:19], row_concat=True)

        # gripper
        processed_action_chunk[:, 14] = action_chunk[:, 9]
        processed_action_chunk[:, 29] = action_chunk[:, 19]

        # send type (is_eef)
        processed_action_chunk[:, 30] = 1.0

        return processed_action_chunk