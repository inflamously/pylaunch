import unittest
from domain.script_provider import module_script_provider
from infrastructure.json_store import module_json_store


class ParserTest(unittest.TestCase):


    json_store = module_json_store.JsonStoreModule(path="./configuration/app/app.config.json")


    def __init__(self, methodName: str=...):
        self.instance = module_script_provider.ScriptProviderModule(
            configuration=self.json_store.configuration["script-provider"], 
            provider="script-provider"
        )
        super().__init__(methodName)


    def test_module_script_provider(self):
        self.assertIsNotNone(self.instance)


    def test_module_script_parse_none(self):
        self.instance.parse()
        self.assertIsNotNone(self.instance.script_provider)


    def test_module_script_parse_empty(self):
        self.instance.parse({})
        self.assertIsNotNone(self.instance.script_provider)


if __name__ == '__main__':
    unittest.main()