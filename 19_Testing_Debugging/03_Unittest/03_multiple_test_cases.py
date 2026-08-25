import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_zero(self):
        self.assertEqual(multiply(0, 6), 0)

    def test_negative_number(self):
        self.assertEqual(multiply(-2, 3), -6)

unittest.main()