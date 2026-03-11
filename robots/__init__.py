"""Robot client registry.

Each client module under robots/<name>/clients/ registers itself by calling register_client()
at module level. The registry is auto-populated by scanning all robots/*/clients/ packages.

Usage in inference.py:
    from robots import CLIENT_REGISTRY
    entry = CLIENT_REGISTRY["bimanual_ur_starvla"]
"""

import importlib
import pkgutil
from pathlib import Path
from typing import Callable, NamedTuple


class ClientEntry(NamedTuple):
    description: str
    factory: Callable  # (args) -> (robot_or_none, client)
    add_arguments: Callable | None = None  # (parser) -> None, for client-specific args


CLIENT_REGISTRY: dict[str, ClientEntry] = {}


def register_client(name: str, description: str, factory: Callable, add_arguments: Callable = None):
    CLIENT_REGISTRY[name] = ClientEntry(description=description, factory=factory, add_arguments=add_arguments)


def _auto_discover():
    """Import all robots/*/clients/*.py modules to trigger their register_client() calls."""
    robots_dir = Path(__file__).parent
    for robot_pkg in sorted(robots_dir.iterdir()):
        clients_dir = robot_pkg / "clients"
        if not (clients_dir.is_dir() and (clients_dir / "__init__.py").exists()):
            continue
        pkg_name = f"robots.{robot_pkg.name}.clients"
        try:
            pkg = importlib.import_module(pkg_name)
        except Exception:
            continue
        for _, mod_name, _ in pkgutil.iter_modules(pkg.__path__):
            try:
                importlib.import_module(f"{pkg_name}.{mod_name}")
            except ImportError:
                # Missing dependencies (e.g. websockets, rtde) — skip silently
                pass
            except Exception as e:
                import logging
                logging.debug(f"Failed to load client module {pkg_name}.{mod_name}: {e}")


_auto_discover()
