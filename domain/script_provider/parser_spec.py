import os
import unittest
from domain.script_provider import provider
from domain.script_provider import parser
from domain.script_provider import exceptions
from infrastructure.json_store import json_store


class ParserTest(unittest.TestCase):
    config_path = "./configuration/app/app.config.json"

    def test_load_config(self):
        config_parser = parser.load_config(self.config_path)
        self.assertIsNotNone(config_parser)


    def test_variable_input_empty(self):
        config_parser = parser.load_config(self.config_path)
        with self.assertRaises(exceptions.EmptyVariable):
            config_parser.assign_variables_with({"":""})            


    def test_variable_input_error_invalid_symbol(self):
        config_parser = parser.load_config(self.config_path)
        with self.assertRaises(exceptions.InvalidVariableSymbol):
            config_parser.assign_variables_with({"$test":"","$test$":""})
            

    def test_variable_parse(self):
        config_parser = parser.load_config(self.config_path)
        # check has variable

        config_parser.assign_variables_with({"$script_provider_path$":"./domain/script_provider"})
        script_provider = config_parser.apply()

        # test variable change

if __name__ == '__main__':
    unittest.main()