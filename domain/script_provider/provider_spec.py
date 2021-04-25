import os
import unittest
from domain.script_provider import provider
from infrastructure.json_store import module_json_store


class ScriptProviderTest(unittest.TestCase):

    test_provider_type = "script-provider"
    json_store = module_json_store.JsonStoreModule(path="./configuration/app/app.config.json")


    def test_config(self):
        self.assertIsNotNone(self.json_store)
        self.assertIsNotNone(self.json_store.configuration)
        self.assertTrue("script-provider" in self.json_store.configuration)


    def test_finder(self):
        script_provider = provider.ScriptProvider(self.json_store.configuration["script-provider"])
        self.assertListEqual(script_provider.search("local-path"), [{'local-path': '$script_provider_path$/local-scripts'}])


if __name__ == '__main__':
    unittest.main()