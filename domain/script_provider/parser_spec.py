import os
import unittest
from domain.script_provider import provider
from domain.script_provider import parser
from domain.script_provider import exceptions
from infrastructure.json_store import json_store


class ParserTest(unittest.TestCase):
    config_path = "./configuration/app/app.config.spec.json"

    def test_load_config(self):
        config_parser = parser.load_config(self.config_path)
        self.assertIsNotNone(config_parser)


    def test_variable_input_empty(self):
        config_parser = parser.load_config(self.config_path)
        with self.assertRaises(exceptions.EmptyVariable):
            config_parser.assign_variables({"":""})            


    def test_variable_input_error_invalid_symbol(self):
        config_parser = parser.load_config(self.config_path)
        with self.assertRaises(exceptions.InvalidVariableSymbol):
            config_parser.assign_variables({"$test":"","$test$":""})
            

    def test_variable_parse(self):
        config_parser = parser.load_config(self.config_path)
        parsed_config = config_parser.assign_variables({"$script_provider_path$":"./domain/script_provider"})
        self.assertDictEqual(parsed_config.config(), {'local-path': './domain/script_provider/local-scripts', 'sync-path': './domain/script_provider/sync-scripts'})


if __name__ == '__main__':
    unittest.main()