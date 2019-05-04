import unittest
from Glass import Glass
import Constants

class TestGlassClass(unittest.TestCase):

	def test_glass_init(self):
		aGlass = Glass(None, None)

		self.assertEqual(None, aGlass.leftChild)
		self.assertEqual(None, aGlass.rightChild)

		self.assertEqual(Constants.GLASS_CAP, aGlass.capacity)

	def test_glass_fillLiquid(self):
		aGlass = Glass(None, None)
		test_overflow = 5
		aGlass.fillLiquid(Constants.GLASS_CAP + test_overflow)
		self.assertEqual(test_overflow, aGlass.overflowed)

	def test_glass_overflowToChildren(self):
		leftChildGlass = Glass(None, None)
		rightChildGlass = Glass(None, None)

		parentGlass = Glass(leftChildGlass, rightChildGlass)

		self.assertEqual(0, leftChildGlass.filled)
		self.assertEqual(0, rightChildGlass.filled)

		test_overflow = 5
		toFill = Constants.GLASS_CAP + test_overflow

		parentGlass.fillLiquid( toFill )
		parentGlass.overflowToChildren()

		self.assertEqual(test_overflow / 2, leftChildGlass.filled )
		self.assertEqual(test_overflow / 2, rightChildGlass.filled )