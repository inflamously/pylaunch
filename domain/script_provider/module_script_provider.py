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

    
    def parser(self, **kwargs) -> generic_provider.GenericProvider:
        if "variables" in kwargs:
            config_parser = parser.ProviderConfigParser(self.script_provider)
            self.script_provider = config_parser.instantiate_provider(kwargs["variables"])