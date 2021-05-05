from fuelstarter import fuelstarter
import eel


from domain.script_provider import module_script_provider
from infrastructure.bridge_frontend import bridge
from infrastructure.json_store import json_store
from infrastructure.json_store import module_json_store


JsonStoreModule = module_json_store.JsonStoreModule(\
    path="./configuration/app/app.config.json")


ScriptProviderModule = module_script_provider.ScriptProviderModule(\
    configuration=JsonStoreModule.configuration["script-provider"],\
        provider="script-provider")


def setup_app():
    bridge.init()
    eel.init(JsonStoreModule.configuration["ui-path"])
    eel.start(JsonStoreModule.configuration["index-file"])


if __name__ == '__main__':
    setup_app()
