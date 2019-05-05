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

		
	def resetState(self):
		self.inputRow = 0
		self.inputCol = 0
		self.inputCapacity = 0

		self.inputStr = ''
		

	def getUserInput(self):
		self.resetState()
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
			num0 = convertStrToInteger(str0)
			if( num0 == Constants.ERROR_CODE ):
				return False
			else:
				self.inputRow = num0

			str1 = strList[1]
			num1 = convertStrToInteger(str1)
			if( num1 == Constants.ERROR_CODE ):
				return False
			else:
				self.inputCol = num1	

			if( self.inputCol > self.inputRow ):
				return False			
		
			str2 = strList[2]
			num2 = convertStrToFloat(str2)
			if( num2 == Constants.ERROR_CODE ):
				return False
			else:
				self.inputCapacity = num2 * 1000	

		return True

	def buildGlassTree(self):
		for rowIndex in reversed(range(self.inputRow+1)):
			for columnIndex in range(rowIndex+1):
				leftChild = None
				rightChild = None

				if( (rowIndex+1, columnIndex) in self.glassTreeDict ):
					leftChild = self.glassTreeDict[(rowIndex+1, columnIndex)]
				if( (rowIndex+1, columnIndex+1) in self.glassTreeDict ):
					rightChild = self.glassTreeDict[(rowIndex+1, columnIndex+1)]

				theGlass = Glass(leftChild,rightChild)
				self.glassTreeDict[(rowIndex, columnIndex)] = theGlass

	def fillGlassTree(self):
		cap = self.inputCapacity
		isRowNoOverflow = False
		hasGlassOverflow = True

		topGlass = self.glassTreeDict[(0,0)]
		topGlass.fillLiquid(cap)

		# if top glass not overflow, stop filling
		if( topGlass.isFull == False ):
			return

		for rowIndex in range(self.inputRow+1):
			if(  hasGlassOverflow == False ):
				break

			hasGlassOverflow = False
			for columnIndex in range(rowIndex+1):
				
				theGlass = self.glassTreeDict[(rowIndex, columnIndex)]
				
				if( theGlass.isFull == True ):
					theGlass.overflowToChildren()
					hasGlassOverflow = True












