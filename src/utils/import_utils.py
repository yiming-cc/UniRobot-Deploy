import pkgutil
import importlib
import logging

def register_local_plugins() -> None:
    # robots
    from src.robots.g1.g1 import G1
    from src.robots.g1.config_g1 import G1Config


    # policies
    from src.policies.xvla_client.modeling_xvla_client import XVLAClientPolicy
    from src.policies.xvla_client.configuration_xvla_client import XVLAClientConfig

    from src.policies.go1_client.modeling_go1_client import GO1ClientPolicy
    from src.policies.go1_client.configuration_go1_client import GO1ClientConfig
