from unittest.mock import patch
import unittest


from Glass import Glass
from App import App
import Constants



class TestAppClass(unittest.TestCase):

    app = None

    @classmethod
    def setUpClass(cls):
        cls.app = App()

    # @patch('__main__.input')
    def test_app_getUserInput(self):        

        mockInputStr = '   3 4 5    ' 

        with patch('builtins.input', return_value=mockInputStr):
            self.app.getUserInput()
            self.assertEqual(mockInputStr, self.app.inputStr)  

    def test_app_isUserValidParams(self):  
        mockInputStr = '   3 4 5    ' 
        self.app.inputStr = mockInputStr

        self.app.isUserValidParams()

        self.assertEqual(3, self.app.inputRow)
        self.assertEqual(4, self.app.inputCol)
        self.assertEqual(5000, self.app.inputCapacity)

        mockInputStr = '   o 4 5    ' 
        self.app.inputStr = mockInputStr

        result = self.app.isUserValidParams()
        self.assertEqual(False, result)







