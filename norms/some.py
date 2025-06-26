import unittest
from Norm_11 import add, is_odd


class TestCalculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2, 3, extra=4), 10)
        self.assertEqual(add(-1, -2, -3, extra=-4), -10)
        self.assertEqual(add(1, 2, -3, extra=-4), -4)

    def test_is_odd(self):
        self.assertFalse(is_odd(0))
        self.assertTrue(is_odd(1))
