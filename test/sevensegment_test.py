import unittest
from sevensegment import SevenSegment


class TestSevenSegment(unittest.TestCase):

    def setUp(self):
        self.sevensegment = SevenSegment()

    def test_check_if_it_on(self):
        self.assertTrue(self.sevensegment.is_on)

    def test_input(self):
        self.sevensegment.splitting_into_array("11111111")

    def test_input1(self):
        self.sevensegment.splitting_into_array("11100110")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.assertEqual(7, self.sevensegment.splitting_into_array("0111111111"))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            self.assertEqual(7, self.sevensegment.splitting_into_array("23313111111"))


if __name__ == '__main__':
    unittest.main()
