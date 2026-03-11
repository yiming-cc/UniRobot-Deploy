import logging
import time

import numpy as np

try:
    import pyrealsense2 as rs
except Exception as e:
    rs = None
    logging.warning(f"Could not import pyrealsense2: {e}")

logger = logging.getLogger(__name__)


class RealSenseCamera:
    """Minimal RealSense camera wrapper for capturing color frames."""

    def __init__(self, serial_number: str, width: int = 640, height: int = 480, fps: int = 30):
        self.serial_number = serial_number
        self.width = width
        self.height = height
        self.fps = fps
        self.pipeline = None
        self.profile = None

    def __str__(self) -> str:
        return f"RealSenseCamera({self.serial_number})"

    @property
    def is_connected(self) -> bool:
        return self.pipeline is not None and self.profile is not None

    def connect(self, warmup_s: float = 1.0):
        if rs is None:
            raise ImportError("pyrealsense2 is not installed")
        if self.is_connected:
            raise RuntimeError(f"{self} is already connected.")

        self.pipeline = rs.pipeline()
        config = rs.config()
        rs.config.enable_device(config, self.serial_number)
        config.enable_stream(rs.stream.color, self.width, self.height, rs.format.rgb8, self.fps)

        try:
            self.profile = self.pipeline.start(config)
        except RuntimeError as e:
            self.pipeline = None
            self.profile = None
            raise ConnectionError(f"Failed to open {self}: {e}") from e

        # Warmup
        time.sleep(warmup_s)
        logger.info(f"{self} connected.")

    def read(self, timeout_ms: int = 200) -> np.ndarray:
        if not self.is_connected:
            raise RuntimeError(f"{self} is not connected.")

        ret, frames = self.pipeline.try_wait_for_frames(timeout_ms=timeout_ms)
        if not ret or frames is None:
            raise RuntimeError(f"{self} read failed.")

        color_frame = frames.get_color_frame()
        return np.asanyarray(color_frame.get_data())

    def disconnect(self):
        if self.pipeline is not None:
            self.pipeline.stop()
            self.pipeline = None
            self.profile = None
            logger.info(f"{self} disconnected.")
