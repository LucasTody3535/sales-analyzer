from unittest import TestCase, main as start_test, defaultTestLoader
from main import hello_world


class HelloWorld(TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello World!")


if __name__ == "__main__":
    start_test()
