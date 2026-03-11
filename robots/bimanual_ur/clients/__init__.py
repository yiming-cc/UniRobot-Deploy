"""Bimanual UR client registration.

All client factories use lazy imports so registration works without heavy dependencies
(websockets, rtde, pyrealsense2, etc.) being installed.
"""

from robots import register_client


# ── StarVLA ──────────────────────────────────────────────────────

def _starvla_add_arguments(parser):
    parser.add_argument("--action_type", type=str, default="joint", choices=["joint", "tcp"])
    parser.add_argument("--execution_steps", type=int, default=16)
    parser.add_argument("--prefix_steps", type=int, default=8)
    parser.add_argument("--rtc", action="store_true", default=True, help="Enable RTC async mode")
    parser.add_argument("--no-rtc", dest="rtc", action="store_false")


def _starvla_factory(args):
    from .starvla_client import StarVLAClient
    from ..config import BimanualURConfig
    from ..bimanual_ur import BimanualUR

    config = BimanualURConfig()
    robot = BimanualUR(config)
    robot.connect()
    client = StarVLAClient(
        host=args.host, port=args.port, robot=robot,
        execution_steps=args.execution_steps, prefix_steps=args.prefix_steps,
        fps=args.fps, rtc=args.rtc, action_type=args.action_type, verbose=args.verbose,
    )
    return robot, client


register_client("bimanual_ur_starvla", "Bimanual UR + StarVLA", _starvla_factory, _starvla_add_arguments)


# ── DreamZero ────────────────────────────────────────────────────

def _dreamzero_add_arguments(parser):
    parser.add_argument("--action_type", type=str, default="joint", choices=["joint", "tcp"])


def _dreamzero_factory(args):
    from .dreamzero_client import DreamZeroClient
    from ..config import BimanualURConfig
    from ..bimanual_ur import BimanualUR

    config = BimanualURConfig()
    robot = BimanualUR(config)
    robot.connect()
    client = DreamZeroClient(
        host=args.host, port=args.port, robot=robot,
        fps=args.fps, action_type=args.action_type, verbose=args.verbose,
    )
    return robot, client


register_client("bimanual_ur_dreamzero", "Bimanual UR + DreamZero", _dreamzero_factory, _dreamzero_add_arguments)
