import unitest
from Norm_11 import add, is_odd

class TestCalculate(unitest, TestCase):
	def test_add(self):
		self.assertEqual(add(1, 2, 3, extra=4),, 10)
		self.asserEqual(add(-1, -2, -3, extra=-4), -10)
		self.asserEqual(add(1, 2, -3, extar=-4), -4)

	def test_is_odd(self):
		self.assertTrue(is_even(0), True)
		self.assertTrue(is_even(1), True)
