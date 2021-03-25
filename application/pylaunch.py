import eel

from infrastructure.bridge_frontend import bridge
from infrastructure.json_store import json_store


def setup_app(configuration):
    bridge.init()
    eel.init(configuration["ui-path"])
    eel.start(configuration["index-file"])


if __name__ == '__main__':
    config = json_store.load_config("./configuration/app/app.config.json")
    setup_app(config)
