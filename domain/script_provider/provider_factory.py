import os
import copy
import abc
from infrastructure.json_store import json_store
from domain.script_provider import exceptions
from domain.script_provider import provider


def factory(config_path, provider_name) -> provider.GenericProvider:
    if provider_name == "" or provider_name == None:
        raise exceptions.InvalidProviderNameProvided(provider_name)
    root_config = json_store.load_config(config_path)
    if provider_name == "ScriptProvider":
        if not "script-provider" in root_config:
            raise exceptions.NoScriptProviderDefined(root_config)
        config_dict = root_config["script-provider"]
        return provider.ScriptProvider(config_dict)
    else:
        raise exceptions.NamedProviderNotImplemented(provider_name)