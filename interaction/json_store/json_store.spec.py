import unittest
import json_store
import os


class TestJsonManager(unittest.TestCase):
    def test_load(self):
        store = json_store.store("./configuration/app/app.config.json")

        with self.assertRaises(FileNotFoundError):
            json_store.load_config("")
            json_store.load_config("qwertz")
            json_store.load_config("pylaunch.py")
            json_store.load_config("./configuration/app.config.spec.jsox")


    def test_save(self):
        with self.assertRaises(FileNotFoundError):
            json_store.save_config("")
            json_store.save_config("qwertz")
            json_store.save_config("./configuration/app.config.spec.jsox")
        self.assertTrue(os.path.exists("./configuration/app/app.config.spec.json"))



if __name__ == '__main__':
    unittest.main()