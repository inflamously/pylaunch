import os
import unittest
from domain.script_provider import provider_factory
from infrastructure.json_store import json_store


class ScriptProviderTest(unittest.TestCase):

    test_provider_type = "script-provider"
    test_config_path = "./configuration/app/app.config.spec.json"


    def test_config(self):
        config = json_store.load_config(self.test_config_path)
        self.assertIsNotNone(config)
        self.assertTrue("script-provider" in config)


    def test_query_config(self):
        script_provider_config = provider_factory.create_provider(self.test_config_path, self.test_provider_type)
        self.assertIsNotNone(script_provider_config)


    def test_finder(self):
        script_provider_config = provider_factory.create_provider(self.test_config_path, self.test_provider_type)
        self.assertListEqual(script_provider_config.search("local-path"), [{'local-path': '$script_provider_path$/local-scripts'}])

if __name__ == '__main__':
    unittest.main()