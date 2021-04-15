from domain.script_provider import provider_factory
from domain.script_provider import provider
from domain.script_provider import exceptions


class ProviderConfigParser():


    def __init__(self, script_provider: provider.GenericProvider):
        if len(script_provider.search("local-path")) <= 0: raise exceptions.ConfigVariableNotFound("local-path")
        if len(script_provider.search("sync-path")) <= 0: raise exceptions.ConfigVariableNotFound("sync-path")
        self.script_provider = script_provider
    

    def assign_variables(self, vars: dict) -> provider.GenericProvider:
        if len(vars) > 0:
            for key in vars.keys():
                if len(key) <= 0: raise exceptions.EmptyVariable(key)
                elif not key[1] == provider.SCRIPT_CONFIG_VAR_SYMBOL and \
                    not key[len(key) - 1] == provider.SCRIPT_CONFIG_VAR_SYMBOL:
                    raise exceptions.InvalidVariableSymbol(key)
                else:
                    return self.__assign_variables(vars)
        raise exceptions.EmptyVariableDictionary


    def __assign_variables(self, vars: dict) -> provider.GenericProvider:
        config = self.script_provider.config()
        for key_config in config.keys():
            for key_var in vars.keys():
                config[key_config] = config[key_config].replace(key_var, vars[key_var])
        return self.script_provider.apply(config)


def load_config(config_path, provider_name) -> ProviderConfigParser:
    config = provider_factory.factory(config_path, provider_name)
    
    return ProviderConfigParser(config)