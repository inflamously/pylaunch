import os
import unittest
from domain.script_provider import provider
from domain.script_provider import parser
from domain.script_provider import exceptions
from infrastructure.json_store import module_json_store


class ParserTest(unittest.TestCase):


    json_store = module_json_store.JsonStoreModule(path="./configuration/app/app.config.spec.json")
    variables = {"$script_provider_path$":"./domain/script_provider"}
    

    def __init__(self, methodName: str=...):
        self.test_script_provider_parser = parser.ProviderConfigParser(provider.ScriptProvider(self.json_store.configuration["script-provider"]))
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
        provider = self.test_script_provider_parser.instantiate_provider(self.variables)
        self.assertDictEqual(provider.config(), {'local-path': './domain/script_provider/local-scripts', 'sync-path': './domain/script_provider/sync-scripts'})


if __name__ == '__main__':
    unittest.main()