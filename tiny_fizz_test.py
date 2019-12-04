import unittest
from tiny_fizz_buzz import tiny_fizz_buzz


class TinyTest(unittest.TestCase):
    def test_tiny(self):
        self.assertEqual(tiny_fizz_buzz('Hello WORLD!'),
                         'IronYardllYard IronIron YardIronIronIron!')


if __name__ == '__main__':
    unittest.main()
