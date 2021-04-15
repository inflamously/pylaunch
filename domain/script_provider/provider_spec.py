import os
import unittest
from domain.script_provider import provider_factory
from infrastructure.json_store import json_store


class ScriptProviderTest(unittest.TestCase):

    config_provider_name = "ScriptProvider"
    config_path = "./configuration/app/app.config.spec.json"


    def test_config(self):
        config = json_store.load_config(self.config_path)
        self.assertIsNotNone(config)
        self.assertTrue("script-provider" in config)


    def test_query_config(self):
        script_provider_config = provider_factory.factory(self.config_path, self.config_provider_name)
        self.assertIsNotNone(script_provider_config)


    def test_finder(self):
        script_provider_config = provider_factory.factory(self.config_path, self.config_provider_name)
        self.assertListEqual(script_provider_config.search("local-path"), [{'local-path': '$script_provider_path$/local-scripts'}])

if __name__ == '__main__':
    unittest.main()