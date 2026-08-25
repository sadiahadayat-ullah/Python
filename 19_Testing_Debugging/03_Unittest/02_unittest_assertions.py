import unittest

class TestAssertion(unittest.TestCase):

    def test(self):
        self.assertEqual(10, 10)
        self.assertNotEqual(20, 10)
        self.assertTrue(10 > 5)
        self.assertFalse(5 > 10)
        self.assertIn("apple", ["apple", "banana"])
        self.assertNotIn("orange", ["apple", "banana"])

unittest.main()