from domain.script_provider import provider
from domain.script_provider import exceptions


class ProviderConfigParser():


    def __init__(self, script_provider: provider.ScriptProvider):
        self.script_provider = script_provider
    

    def assign_variables_with(self, vars: dict):
        if len(vars) > 0:
            for key in vars.keys():
                if len(key) <= 0: raise exceptions.EmptyVariable(key)
                elif not key[1] == provider.SCRIPT_CONFIG_VAR_SYMBOL and \
                    not key[len(key) - 1] == provider.SCRIPT_CONFIG_VAR_SYMBOL:
                    raise exceptions.InvalidVariableSymbol(key)
                else:
                    self.__assign_variables(vars)


    def __assign_variables(self, vars: dict):
        config = self.script_provider.config
        for key_config in config.keys():
            for key_var in vars.keys():
                config[key_config] = config[key_config].replace(key_var, vars[key_var])
        self.script_provider.config = config


    def apply(self) -> provider.ScriptProvider:
        return self.script_provider


def load_config(path):
    config = provider.query_config(path)
    
    return ProviderConfigParser(config)