import Constants

def convertStrToInteger(aStr):
	val = 0
	try:
	   val = int(aStr)
	except ValueError:
	   return Constants.ERROR_CODE

	if( val < 0 ):
		return Constants.ERROR_CODE
	else:
		return val
	
def convertStrToFloat(aStr):
	val = 0
	try:
	   val = float(aStr)
	except ValueError:
	   return Constants.ERROR_CODE

	if( val < 0 ):
		return Constants.ERROR_CODE
	else:
		return val


