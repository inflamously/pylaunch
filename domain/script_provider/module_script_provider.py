from domain.script_provider import provider
from domain.script_provider import generic_provider
from domain.script_provider import parser


class ScriptProviderModule:


    def __init__(self, **kwargs):
        if "configuration" in kwargs:
            self.configuration = kwargs["configuration"]
        if "provider" in kwargs:
            if kwargs["provider"] == "script-provider":
                self.script_provider = provider.ScriptProvider(self.configuration)
                self.parse()

    
    def parse(self, variables: dict=None) -> generic_provider.GenericProvider:
        if variables or \
           "variables" in self.configuration:
            custom_vars = variables if variables else self.configuration["variables"]

            config_parser = parser.ProviderConfigParser(self.script_provider)
            self.script_provider = config_parser.instantiate_provider(custom_vars)