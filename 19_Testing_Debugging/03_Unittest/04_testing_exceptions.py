import unittest

def divide(a, b):
    return a / b

class TestDivide(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

unittest.main()