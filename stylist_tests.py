import unittest
import mycode


class StylistTests(unittest.TestCase):
    def tests_style_hello(self):
        self.assertEqual(hello_world(), 'Hello World')


if __name__ == '__main__':
    unittest.main()
