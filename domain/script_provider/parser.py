from domain.script_provider import generic_provider
from domain.script_provider import exceptions


class ProviderConfigParser():


    def __init__(self, script_provider: generic_provider.GenericProvider):
        self.script_provider = script_provider
    

    def instantiate_provider(self, variables: dict) -> generic_provider.GenericProvider:
        if len(variables) > 0:
            for key in variables.keys():
                if len(key) <= 0: raise exceptions.EmptyVariable(key)
                elif not key[1] == generic_provider.SCRIPT_CONFIG_VAR_SYMBOL and \
                    not key[len(key) - 1] == generic_provider.SCRIPT_CONFIG_VAR_SYMBOL:
                    raise exceptions.InvalidVariableSymbol(key)
                else:
                    return self.__assign_variables(variables)
        raise exceptions.EmptyVariableDictionary


    def __assign_variables(self, variables: dict) -> generic_provider.GenericProvider:
        config = self.script_provider.config()

        for key_config in config.keys():
            for key_var in variables.keys():
                if isinstance(config[key_config], str):
                    config[key_config] = config[key_config].replace(key_var, variables[key_var])
        return self.script_provider.apply(config)