import unittest
from app import HelloWorld


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.hello_world = HelloWorld()
        self.output = self.hello_world.get()

    def test_get_hello_world(self):
        expected = 'Hello World!'
        self.assertEqual(self.output, expected)

    def fail_test_get_hello_world(self):
        expected = 'Ciao Mondo!'
        self.assertIsNot(self.output, expected)

if __name__ == '__main__':
    unittest.main()