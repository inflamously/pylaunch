from fuelstarter import fuelstarter
import eel


from domain.script_provider import provider
from infrastructure.bridge_frontend import bridge
from infrastructure.json_store import json_store
from application import pylaunch_global


def setup_app(configuration):
    bridge.init()
    pylaunch_global.provider_setup(configuration, {"$script_provider_path$":"./domain/script_provider"})
    eel.init(configuration["ui-path"])
    eel.start(configuration["index-file"])


if __name__ == '__main__':
    config = json_store.load_config("./configuration/app/app.config.json")
    setup_app(config)
