import os
from infrastructure.json_store import json_store


def validate_paths(script_provider):
    return "local-path" in script_provider and "sync-path" in script_provider


def query_config(path):
    return json_store.load_config(path)["script-provider"]


def local_scripts(script_provider):
    return os.listdir(script_provider["local-path"])
