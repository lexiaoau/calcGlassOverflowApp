#!/usr/bin/python3
import Constants

class Glass:
 
    def __init__(self, leftC, rightC):
      self.leftChild = leftC 
      self.rightChild = rightC      

      self.capacity = Constants.GLASS_CAP       # liquid capacity(in ml) of each glass
      self.filled = 0.0                         # how much liquid currently filled
      self.overflowed = 0.0                     # how much liquid currently overflowed
      self.isFull = False                       # is the glass full

    # fill glass with amount liquid
    # if overfilled, set overflow amount and set this as full
    def fillLiquid(self, amount):
        self.filled = self.filled + amount
        if( self.filled > self.capacity ):
            self.overflowed = self.overflowed + (self.filled - self.capacity)       # plus previous overflow value for reentry
            self.filled = self.capacity
            self.isFull = True

    # send overflow evenly to both child
    def overflowToChildren(self):
        if( self.leftChild is None or self.rightChild is None  ):
            return
        elif ( self.overflowed <= 0 ):
            print("Error: not overflowed")
        else:
            self.leftChild.fillLiquid( self.overflowed / 2 )
            self.rightChild.fillLiquid( self.overflowed / 2 )
