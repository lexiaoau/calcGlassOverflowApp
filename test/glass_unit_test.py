import unittest
from Glass import Glass
import Constants

class TestGlassClass(unittest.TestCase):

	def test_glass_init(self):
		aGlass = Glass(None, None)

		self.assertEqual(None, aGlass.leftChild)
		self.assertEqual(None, aGlass.rightChild)

		self.assertEqual(Constants.GLASS_CAP, aGlass.capacity)