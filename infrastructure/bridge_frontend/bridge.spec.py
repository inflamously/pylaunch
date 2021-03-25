import unittest
import bridge


class BridgeTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(bridge.debug_sum(2, 2), 4)

    def test_hello(self):
        self.assertEqual(bridge.debug_hello(), "Hello World, from Python by EEL.")

    def test_void(self):
        bridge.debug_void()


if __name__ == '__main__':
    unittest.main()