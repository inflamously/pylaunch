import copy
import abc


SCRIPT_CONFIG_VAR_SYMBOL = "$"


class GenericProvider(abc.ABC):


    @abc.abstractmethod
    def config(self):
        ...


class ScriptProvider(GenericProvider):
    

    def __find(self, flatlist, search_string, config):
        for variable in config:
            if type(config[variable]) is dict:
                self.__find(flatlist, config[variable], search_string)
            else:
                if search_string in config and search_string == variable:
                    flatlist.append({search_string: config[variable]})


    def search(self, search_string) -> list:
        flat_configuration = []
        self.__find(flat_configuration, search_string, self.__config)
        return flat_configuration


    def config(self):
        return copy.deepcopy(self.__config)


    def apply(self, config):
        return ScriptProvider(config)


    def __init__(self, config: dict):
        self.__config = config

    
    def __str__(self):
        return str(self.__config)