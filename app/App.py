#!/usr/bin/python3
import Constants
from Glass import Glass
from Util import *

class App:
	def __init__(self):
		self.glassTreeDict = {}		# dict to simulate glass tree
		self.inputRow = 0
		self.inputCol = 0
		self.inputCapacity = 0	# input unit is litre, need to convert to ml

		self.exit = False       # exit program?
		self.inputStr = ''		# accept user input from command line

		
	# reset all user input related state to init
	def resetState(self):
		self.inputRow = 0
		self.inputCol = 0
		self.inputCapacity = 0

		self.inputStr = ''
		
	# get user input from command line and save to object variable
	def getUserInput(self):
		self.resetState()
		msg1 = 'To calculate j’th glass of the i’th row when K litres are poured into the top most glass, please enter "i j K" in below line(seperated with white space.)'
		msg2 = 'Or you can enter "exit" to exit this program.'
		print(msg1)
		print(msg2)

		self.inputStr = input(">>> ")		

	# check is user want to exit program
	def isUserInputExit(self):
		userInput = self.inputStr.strip()
		if( userInput == "exit"):
			return True
		else:
			return False

	# check user input values, if valid then assigne to object variables
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

			# in glass tree, column number can not be greater than row number
			if( self.inputCol > self.inputRow ):
				return False			
		
			str2 = strList[2]
			num2 = convertStrToFloat(str2)
			if( num2 == Constants.ERROR_CODE ):
				return False
			else:
				self.inputCapacity = num2 * 1000	# convert L to ml

		return True

	# build a glass tree from bottom up
	# associate each glass with its two children if they exist
	# when glass created, put it into dict using tuple (row, column) as key 
	def buildGlassTree(self):
		for rowIndex in reversed(range(self.inputRow+1)):
			for columnIndex in range(rowIndex+1):
				leftChild = None
				rightChild = None

				if( (rowIndex+1, columnIndex) in self.glassTreeDict and (rowIndex+1, columnIndex+1) in self.glassTreeDict ):
					leftChild = self.glassTreeDict[(rowIndex+1, columnIndex)]
					rightChild = self.glassTreeDict[(rowIndex+1, columnIndex+1)]

				theGlass = Glass(leftChild,rightChild)
				self.glassTreeDict[(rowIndex, columnIndex)] = theGlass

	# from top, fill glass tree with "cap" liquid
	# loop from top row to lower row
	# if no glass in one row overflow, stop the loop
	def fillGlassTree(self):
		cap = self.inputCapacity
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
					hasGlassOverflow = True				# mark glass with overflow
					theGlass.overflowToChildren()
					
	# entry function to run this app
	# loop to accept user input values until input "exit"
	# if input values valid, build glass tree and fill liquid, then print filled amount of user specified glass
	def runApp(self):
		isExit = False
		while(not isExit):
			self.getUserInput()
			if( self.isUserInputExit() ):
				isExit = True
			else:
				if( self.isUserValidParams() ):
					self.buildGlassTree()
					self.fillGlassTree()
					theGlass = self.glassTreeDict[(self.inputRow, self.inputCol)]
					print("<<< The {}th glass of row {} is filled with {}ml.".format(self.inputCol, self.inputRow, theGlass.filled))
				else:
					print("Input invalid. Please check and input again.")

if __name__== "__main__":
	app = App()
	app.runApp()


