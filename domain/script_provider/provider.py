import copy
import glob
import os
from domain.script_provider import generic_provider


class ScriptProvider(generic_provider.GenericProvider):


    __config: dict = None


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


    def query_scripts(self):
        if not os.path.exists(self.__config["local-path"]): raise ScriptProviderException("Path '" + self.__config["local-path"] + "' does not exist.")
        else:
            scripts = []
            return scripts
            # for script in glob.glob("**/*.py"):
            #     ...
            # print("Script:", local_path.parent)
    
    def __str__(self):
        return str(self.__config)


class ScriptProviderException(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(message)
