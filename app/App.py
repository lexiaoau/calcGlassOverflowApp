import Constants
from Glass import Glass

class App:
	def __init__(self):
		self.glassTreeDict = {}
		self.inputRow = 0
		self.inputCol = 0
		self.inputCapacity = 0	# input unit is litre, need to convert to ml

		self.exit = False
		self.inputStr = ''

	def getUserInput(self):
		msg1 = 'To calculate j’th glass of the i’th row when K litres are poured into the top most glass, please enter "i j K" in below line(seperated with white space.)'
		msg2 = 'Or you can enter "exit" to exit this program.'
		print(msg1)
		print(msg2)

		self.inputStr = input(">>> ")
		print('|'+self.inputStr+'|')


