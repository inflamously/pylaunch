import os
import unittest
from domain.script_provider import script_provider
from infrastructure.json_store import json_store


class ScriptProviderTest(unittest.TestCase):


    config_path = "./configuration/app/app.config.json"


    def test_config(self):
        config = json_store.load_config(self.config_path)
        self.assertIsNotNone(config)
        self.assertTrue("script-provider" in config)


    def test_query_config(self):
        script_provider_config = script_provider.query_config(self.config_path)
        self.assertIsNotNone(script_provider_config)
        self.assertTrue("local-path" in script_provider_config)
        self.assertTrue("sync-path" in script_provider_config)


if __name__ == '__main__':
    unittest.main()