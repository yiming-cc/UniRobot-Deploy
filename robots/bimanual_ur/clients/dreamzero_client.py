"""DreamZero client for bimanual UR — placeholder for future implementation."""

import logging
from typing import Optional

import numpy as np

logger = logging.getLogger(__name__)


class DreamZeroClient:
    """DreamZero client with bimanual UR hardware control.

    TODO: Implement the actual DreamZero inference protocol.
    Must expose: step(task_description, fps, ...), close(), and optionally go_home().
    """

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: Optional[int] = None,
        robot=None,
        fps: int = 30,
        action_type: str = "joint",
        verbose: bool = False,
    ):
        self.host = host
        self.port = port
        self.robot = robot
        self.fps = fps
        self.action_type = action_type
        self.verbose = verbose
        raise NotImplementedError("DreamZeroClient is not yet implemented")

    def step(self, task_description=None, fps=None, action_type=None, view_mask=None):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError
