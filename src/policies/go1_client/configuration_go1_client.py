from dataclasses import dataclass, field
from lerobot.configs.policies import PreTrainedConfig
from lerobot.configs.types import NormalizationMode
from lerobot.optim.optimizers import AdamConfig
from lerobot.optim.schedulers import DiffuserSchedulerConfig


@PreTrainedConfig.register_subclass("go1_client")
@dataclass
class GO1ClientConfig(PreTrainedConfig):
    # Inputs / output structure.
    n_obs_steps: int = 2
    horizon: int = 16
    n_action_steps: int = 8

    url: str | None = None
    host: str | None = None
    port: int | None = None

    
    def __post_init__(self):
        super().__post_init__()
        # Add any validation logic here

    def validate_features(self) -> None:
        """Validate input/output feature compatibility."""
        # Implement validation logic for your policy's requirements
        pass

    @property
    def observation_delta_indices(self) -> list:
        return list(range(1 - self.n_obs_steps, 1))

    @property
    def action_delta_indices(self) -> list:
        return list(range(1 - self.n_obs_steps, 1 - self.n_obs_steps + self.horizon))

    @property
    def reward_delta_indices(self) -> None:
        return None

    
    def get_optimizer_preset(self) -> AdamConfig:
        return None

    def get_scheduler_preset(self) -> DiffuserSchedulerConfig:
        return None
