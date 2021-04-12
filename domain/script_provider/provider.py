import os
from infrastructure.json_store import json_store


SCRIPT_CONFIG_VAR_SYMBOL = "$"


class ScriptProvider():
    def __init__(self, config: dict):
        self.config = config

    
    def __str__(self):
        return str(self.config)


def validate_paths(script_provider):
    return "local-path" in script_provider and "sync-path" in script_provider


def query_config(path):
    config_dict = json_store.load_config(path)["script-provider"]

    return ScriptProvider(config_dict)


def local_scripts(script_provider):
    return os.listdir(script_provider["local-path"])
