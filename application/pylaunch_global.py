from domain.script_provider import provider
from domain.script_provider import parser


class __PylaunchProviderContainer:
    def __init__(self): 
        ...


providers = __PylaunchProviderContainer()


def provider_setup(configuration: dict, variables: dict) -> None:
    providers.script_provider = parser.ProviderConfigParser(provider.ScriptProvider(configuration["script-provider"])).instantiate_provider(variables)