import unittest

from convert import itoa, atoi


class ConvertTest(unittest.TestCase):
    def test_atoi_positive_integer(self):
        self.assertEqual(atoi("1"), 1)

    def test_atoi_zero_integer(self):
        self.assertEqual(atoi("0"), 0)

    def test_atoi_negative_integer(self):
        self.assertEqual(atoi("-2"), -2)

    def test_atoi_decimal(self):
        with self.assertRaises(ValueError):
            self.assertEqual(atoi("0.0"), 0)

    def test_atoi_string(self):
        with self.assertRaises(ValueError):
            atoi("fish")

    def test_itoa_positive_integer(self):
        self.assertEqual(itoa(1), "1")

    def test_itoa_zero_integer(self):
        self.assertEqual(itoa(0), "0")

    def test_itoa_negative_integer(self):
        self.assertEqual(itoa(-10), "-10")

    def test_itoa_decimal(self):
        with self.assertRaises(ValueError):
            itoa(9.2)

    def test_itoa_list(self):
        with self.assertRaises(ValueError):
            itoa([32])


if __name__ == '__main__':
    unittest.main()
