import os
import unittest
from domain.script_provider import provider
from domain.script_provider import parser
from infrastructure.json_store import module_json_store


class ScriptProviderTest(unittest.TestCase):

    
    json_store = module_json_store.JsonStoreModule(path="./configuration/app/app.config.json")
    variables = {
        "$script_provider_path$": "./domain/script_provider"
    }

    def __init__(self, methodName: str=...):
        self.script_provider = \
            parser.ProviderConfigParser(\
                provider.ScriptProvider(self.json_store.configuration["script-provider"]))\
                    .instantiate_provider(self.variables)
        super().__init__(methodName)


    def test_config(self):
        self.assertIsNotNone(self.json_store)
        self.assertIsNotNone(self.json_store.configuration)
        self.assertTrue("script-provider" in self.json_store.configuration)


    def test_finder(self):
        self.assertListEqual(self.script_provider.search("local-path"), [{'local-path': './domain/script_provider/local-scripts'}])

    
    def test_query_scripts(self):
        self.script_provider.query_scripts()


if __name__ == '__main__':
    unittest.main()