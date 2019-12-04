import unittest
from tiny_fizz_buzz import *


class TinyFizzBuzz(unittest.TestCase):
    def test_tiny_fizz_buzz(self):
        self.assertEqual(tiny_fizz_buzz('Hello WORLD!'),
                         'IronYardllYard IronIron YardIronIronIron!')


if __name__ == '__main__':
    unittest.main()
