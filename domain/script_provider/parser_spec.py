import os
import unittest
from domain.script_provider import provider
from domain.script_provider import parser
from domain.script_provider import exceptions
from infrastructure.json_store import json_store


class ParserTest(unittest.TestCase):


    test_config_path = "./configuration/app/app.config.spec.json"
    test_provider_parser_config = {"$script_provider_path$":"./domain/script_provider"}
    

    def __init__(self, methodName: str=...):
        self.test_script_provider_parser = parser.load_config(self.test_config_path)
        super().__init__(methodName)


    def test_load_config(self):
        self.assertIsNotNone(self.test_script_provider_parser)


    def test_variable_input_empty(self):
        with self.assertRaises(exceptions.EmptyVariable):
            self.test_script_provider_parser.instantiate_provider({"":""})            


    def test_variable_input_error_invalid_symbol(self):
        with self.assertRaises(exceptions.InvalidVariableSymbol):
            self.test_script_provider_parser.instantiate_provider({"$test":"","$test$":""})
            

    def test_parser(self):
        provider = self.test_script_provider_parser.instantiate_provider(self.test_provider_parser_config)
        self.assertDictEqual(provider.config(), {'local-path': './domain/script_provider/local-scripts', 'sync-path': './domain/script_provider/sync-scripts'})


if __name__ == '__main__':
    unittest.main()