import unittest
from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

unittest.main()