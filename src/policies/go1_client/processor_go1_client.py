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

from .configuration_go1_client import GO1ClientConfig

import json_numpy
from src.utils.rotation_utils import RotationConverter
from PIL import Image

EPS = 1e-6


def make_go1_client_pre_post_processors(
    config: GO1ClientConfig,
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
        """convert G1 batch data to go1 client input data
        """

        # image prepare
        main_view = (batch["observation.images.head"][0].permute(1, 2, 0).cpu().numpy()* 255).astype(np.uint8)
        hand_left = (batch["observation.images.hand_left"][0].permute(1, 2, 0).cpu().numpy()* 255).astype(np.uint8)
        hand_right = (batch["observation.images.hand_right"][0].permute(1, 2, 0).cpu().numpy()* 255).astype(np.uint8)

        # Image.fromarray(main_view).save("res/camera_head.png")
        # Image.fromarray(hand_left).save("res/camera_hand_left.png")
        # Image.fromarray(hand_right).save("res/camera_hand_right.png")

        # state prepare
        proprio = np.zeros(16) # [..., (7joints+gripper)*2]
        observation_state = batch["observation.state"][0].cpu().numpy() # observation_features

        # joints
        proprio[0:7] = observation_state[6:13]
        proprio[8:15] = observation_state[20:27]

        # gripper
        proprio[7] = observation_state[13]
        proprio[15] = observation_state[27]

        proprio = np.expand_dims(proprio, axis=0)

        return {
            "state": json_numpy.dumps(proprio),
            "instruction": batch["task"],
            "top": json_numpy.dumps(main_view),
            "left": json_numpy.dumps(hand_left),
            "right": json_numpy.dumps(hand_right),
            "ctrl_freqs": json_numpy.dumps(np.array([30])),
        }

    def backward_process(self, action_chunk: np.ndarray) -> np.ndarray:
        """convert action chunk from GO1 to action features

        Args:
            action_chunk: [..., 16]
        Returns:
            processed_action_chunk: [..., 31]
        """

        processed_action_chunk = np.zeros((action_chunk.shape[0], 31))

        # joints
        processed_action_chunk[:, 7:14] = action_chunk[:, 0:7]
        processed_action_chunk[:, 22:29] = action_chunk[:, 8:15]

        # gripper
        processed_action_chunk[:, 14] = action_chunk[:, 7]
        processed_action_chunk[:, 29] = action_chunk[:, 15]

        # send type (is_eef)
        processed_action_chunk[:, 30] = 0.0

        return processed_action_chunk