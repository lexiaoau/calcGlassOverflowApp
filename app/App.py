import Constants
from Glass import Glass

class App:
	def __init__(self):
		self.glassTreeDict = {}
		self.inputRow = 0
		self.inputCol = 0
		self.inputCapacity = 0	# input unit is litre, need to convert to ml