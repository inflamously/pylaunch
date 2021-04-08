import os
import unittest
from domain.script_provider import script_provider


class ScriptProviderTest(unittest.TestCase):
    def test_path(self):
        self.assertTrue(script_provider.validate_paths())


if __name__ == '__main__':
    unittest.main()