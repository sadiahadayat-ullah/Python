import unittest

class TestNumber(unittest.TestCase):

    def setUp(self):
        self.numbers = [10, 20, 30]
        print("Setting Up")

    def test_length(self):
        self.assertEqual(len(self.numbers), 3)

    def test_first_number(self):
        self.assertEqual(self.numbers[0], 10)

    def tearDown(self):
        print("Cleaning Up")

unittest.main()