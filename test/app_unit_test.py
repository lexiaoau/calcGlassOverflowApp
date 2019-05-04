import unittest
from Glass import Glass
from App import App
import Constants

class TestAppClass(unittest.TestCase):

	def test_app_getUserInput(self):
		app = App()

		row = 3
		col = 4
		cap = 5

		app.getUserInput(row, col, cap)

		self.assertEqual(row, app.inputRow)
		self.assertEqual(col, app.inputCol)
		self.assertEqual(cap*1000, app.inputCapacity)

		
