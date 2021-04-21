from infrastructure.json_store import json_store
from domain.script_provider import exceptions
from domain.script_provider import provider
from domain.script_provider import generic_provider


def create_provider(config_path, provider_type) -> generic_provider.GenericProvider:
    
    
    if not config_path: 
        raise exceptions.NoConfigPathProvided(config_path, provider_type)
    if not provider_type or len(provider_type) <= 0:
        raise exceptions.ProviderTypeInvalidOrNone(config_path, provider_type)

    config = json_store.load_config(config_path)

    if provider_type == "script-provider" and provider_type in config:
        return provider.ScriptProvider(config[provider_type])
    else:
        return None