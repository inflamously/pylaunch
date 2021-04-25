import unittest
from domain.script_provider import module_script_provider
from infrastructure.json_store import module_json_store


class ParserTest(unittest.TestCase):


    json_store = module_json_store.JsonStoreModule(path="./configuration/app/app.config.json")


    def test_module_script_provider(self):
        instance = module_script_provider.ScriptProviderModule(
            configuration=self.json_store.configuration["script-provider"], 
            provider="script-provider")
        instance.parser(variables={"$script_provider_path$":"./domain/script_provider"})
        self.assertIsNotNone(instance)
        self.assertIsNotNone(instance.script_provider)


if __name__ == '__main__':
    unittest.main()