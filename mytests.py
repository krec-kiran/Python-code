import unittest
from mycode import *


class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'Hello World')

    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(5)), 5)


if __name__ == '__main__':
    unittest.main()
