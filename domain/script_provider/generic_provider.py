import abc


SCRIPT_CONFIG_VAR_SYMBOL = "$"


class GenericProvider(abc.ABC):


    @abc.abstractmethod
    def config(self):
        ...