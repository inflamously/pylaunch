from infrastructure.bridge_frontend import bridge_config
from infrastructure.bridge_frontend import bridge_debug


def init():
    bridge_config.init()
    bridge_debug.init()