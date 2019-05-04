import Constants
from Glass import Glass
from Util import *

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

	def isUserInputExit(self):
		userInput = self.inputStr.strip()
		if( userInput == "exit"):
			return True
		else:
			return False



	def isUserValidParams(self):
		userInput = self.inputStr.strip()
		strList = userInput.split()

		if( len(strList) != 3 ):
			return False
		else:
			str0 = strList[0]
			num0 = convertStrToNumber(str0)
			if( num0 == Constants.ERROR_CODE ):
				return False
			else:
				self.inputRow = num0

			str1 = strList[1]
			num1 = convertStrToNumber(str1)
			if( num1 == Constants.ERROR_CODE ):
				return False
			else:
				self.inputCol = num1				
		
			str2 = strList[2]
			num2 = convertStrToNumber(str2)
			if( num2 == Constants.ERROR_CODE ):
				return False
			else:
				self.inputCapacity = num2 * 1000	

		return True

