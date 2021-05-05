import abc
import typing
from domain.script_provider import generic_script


SCRIPT_CONFIG_VAR_SYMBOL = "$"

ScriptCollection = typing.List[generic_script.GenericScript]


class GenericProvider(abc.ABC):


    @abc.abstractmethod
    def search(self, search_string):
        ...


    @abc.abstractmethod
    def config(self):
        ...

    
    @abc.abstractmethod
    def apply(self):
        ...


    @abc.abstractmethod
    def query_scripts(self) -> ScriptCollection:
        ...