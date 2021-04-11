import os
import unittest
from domain.script_provider import script_provider
from infrastructure.json_store import json_store


class ScriptProviderTest(unittest.TestCase):
    def test_config(self):
        config = json_store.load_config("./configuration/app/app.config.json")
        self.assertIsNotNone(config)
        self.assertTrue("script-provider" in config)


    def test_query_config(self):
        script_provider_config = script_provider.query_config("./configuration/app/app.config.json")
        self.assertIsNotNone(script_provider_config)
        self.assertTrue("local-path" in script_provider_config)
        self.assertTrue("sync-path" in script_provider_config)


    def test_path(self):
        script_provider_config = script_provider.query_config("./configuration/app/app.config.json")
        self.assertTrue(script_provider.validate_paths(script_provider_config))


    def test_get_scripts(self):
        script_provider_config = script_provider.query_config("./configuration/app/app.config.json")
        scripts = script_provider.local_scripts(script_provider_config)
        self.assertIsNotNone(scripts)
        self.assertTrue(len(scripts) > 0)


if __name__ == '__main__':
    unittest.main()