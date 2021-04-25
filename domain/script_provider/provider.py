import copy
from domain.script_provider import generic_provider


class ScriptProvider(generic_provider.GenericProvider):


    def __init__(self, config: dict):
        self.__config = config


    def __find(self, flatlist, search_string: str, config: dict):
        if not config or len(config) <= 0: raise ScriptProviderException("No config available.")
        for variable in config:
            if isinstance(config, str): 
                if search_string == config:
                    flatlist.append({search_string: config})
            if isinstance(config, dict): 
                if isinstance(config[variable], dict):
                    self.__find(flatlist, search_string, config[variable])
                elif search_string in config and search_string == variable:
                    flatlist.append({search_string: config[variable]})


    def search(self, search_string) -> list:
        flatlist = []
        self.__find(flatlist, search_string, self.__config)
        return flatlist


    def config(self):
        return copy.deepcopy(self.__config)


    def apply(self, config):
        return ScriptProvider(config)


    def scripts(self):
        # TODO: Implements script instance creation and handles various cases by various classes LocalScriptProvider, RemoteScriptProvider...
        ...

    
    def __str__(self):
        return str(self.__config)


class ScriptProviderException(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(message=message)
