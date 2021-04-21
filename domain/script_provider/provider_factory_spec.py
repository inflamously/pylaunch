import os
import unittest
from domain.script_provider import provider_factory
from domain.script_provider import provider
from domain.script_provider import exceptions


class ProviderFactoryTest(unittest.TestCase):


    test_config_path = "./configuration/app/app.config.json"
    test_provider_type = "script-provider"


    def test_load_script_provider(self):
        script_provider = provider_factory.create_provider(self.test_config_path, self.test_provider_type)
        self.assertIsInstance(script_provider, provider.ScriptProvider)


    def test_no_config_path(self):
        with self.assertRaises(exceptions.NoConfigPathProvided):
            provider_factory.create_provider(None, self.test_config_path)


    def test_no_provider_type(self):
        with self.assertRaises(exceptions.ProviderTypeInvalidOrNone):
            provider_factory.create_provider(self.test_config_path, None)


    def test_non_existing_type(self):
        fun_provider = provider_factory.create_provider(self.test_config_path, "fun-provider")
        self.assertIsNone(fun_provider)


if __name__ == '__main__':
    unittest.main()