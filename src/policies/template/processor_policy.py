from lerobot.processor import (
    PolicyProcessorPipeline,
    PolicyAction,
    ProcessorStep,
)

from dataclasses import dataclass
from typing import Any

import numpy as np
import torch

from .configuration_policy import PolicyTemplateConfig

def make_template_pre_post_processors(
    config: PolicyTemplateConfig,
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
        ),
    )
