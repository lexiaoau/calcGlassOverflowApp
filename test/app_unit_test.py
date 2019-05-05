#!/usr/bin/python3
from unittest.mock import patch
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../app")

from Glass import Glass
from App import App

class TestAppClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = App()             # app instance to run test on

    def test_app_getUserInput(self):        

        mockInputStr = '   3 3 5    ' 

        # mock builtins input function to test user input value
        with patch('builtins.input', return_value=mockInputStr):
            self.app.getUserInput()
            self.assertEqual(mockInputStr, self.app.inputStr)  

    def test_app_isUserValidParams(self):  
        mockInputStr = '   3 3 5    ' 
        self.app.inputStr = mockInputStr

        self.app.isUserValidParams()

        self.assertEqual(3, self.app.inputRow)
        self.assertEqual(3, self.app.inputCol)
        self.assertEqual(5000, self.app.inputCapacity)

        # test invalid input and reset
        mockInputStr = '   o 4 5    ' 
        self.app.inputStr = mockInputStr

        result = self.app.isUserValidParams()
        self.assertEqual(False, result)

    def test_app_buildGlassTree(self): 
        rowNum = 5
        self.app.inputRow = rowNum
        self.app.buildGlassTree()

        self.assertEqual((rowNum+1)*(rowNum+2)/2 , len(self.app.glassTreeDict))     # total triangel glass count should be row*(row+1)/2

        # test children association
        self.assertEqual( (self.app.glassTreeDict[(4,1)]).leftChild , self.app.glassTreeDict[(5,1)] )
        self.assertEqual( (self.app.glassTreeDict[(4,1)]).rightChild , self.app.glassTreeDict[(5,2)] )

    # test buildTree and fill, and verify each glass with correct filled amount
    def test_app_fillGlassTree(self): 
        rowNum = 6
        self.app.inputRow = rowNum


        self.app.buildGlassTree()
        self.app.inputCapacity = 750
        self.app.fillGlassTree()

        self.assertEqual( 250 , (self.app.glassTreeDict[(0,0)]).filled )
        self.assertEqual( 250 , (self.app.glassTreeDict[(1,1)]).filled )
        self.assertEqual( 0 , (self.app.glassTreeDict[(3,0)]).filled )



        self.app.buildGlassTree()
        self.app.inputCapacity = 2250
        self.app.fillGlassTree()

        self.assertEqual( 250 , (self.app.glassTreeDict[(0,0)]).filled )
        self.assertEqual( 250 , (self.app.glassTreeDict[(3,2)]).filled )
        self.assertEqual( 62.5 , (self.app.glassTreeDict[(3,0)]).filled )
        self.assertEqual( 31.25 , (self.app.glassTreeDict[(4,1)]).filled )
        self.assertEqual( 62.5 , (self.app.glassTreeDict[(4,2)]).filled )

        self.app.buildGlassTree()
        self.app.inputCapacity = 5000
        self.app.fillGlassTree()

        self.assertEqual( 78.125 , (self.app.glassTreeDict[(4,0)]).filled )
        self.assertEqual( 179.6875 , (self.app.glassTreeDict[(6,2)]).filled )



