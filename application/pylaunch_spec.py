import os
import unittest
import pylaunch
from adapter.json_store import json_store


class TestPylaunch(unittest.TestCase):
    def test_app_config(self):
        store = json_store.store("./configuration/app/app.config.json")

        self.assertTrue("ui-path" in store)
        self.assertTrue("index-file" in store)


if __name__ == '__main__':
    unittest.main()