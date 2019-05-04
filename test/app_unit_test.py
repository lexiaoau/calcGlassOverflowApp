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

    @patch('__main__.input')
    def test_app_getUserInput(self, mock_input):        

        mockInputStr = '   3 4 5    ' 

        with patch('builtins.input', return_value=mockInputStr):
            self.app.getUserInput()
            self.assertEqual(mockInputStr, self.app.inputStr)  

  
