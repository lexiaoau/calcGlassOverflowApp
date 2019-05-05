import Constants

class Glass:
 
    def __init__(self, leftC, rightC):
      self.leftChild = leftC 
      self.rightChild = rightC 
      # self.leftParent = None
      # self.rightParent = None

      self.capacity = Constants.GLASS_CAP
      self.filled = 0.0
      self.overflowed = 0.0
      self.isFull = False

      # self.outMost = False

      # if( self.leftParent is None or self.rightParent is None ):
      #   self.outMost = True


    # fill glass with amount liquid
    # if overfilled, set overflow amount and set this as full
    def fillLiquid(self, amount):
        self.filled = self.filled + amount
        if( self.filled > self.capacity ):
            self.overflowed = self.overflowed + (self.filled - self.capacity)
            self.filled = self.capacity
            self.isFull = True

    # send overflow evenly to both child
    def overflowToChildren(self):
        if( self.leftChild is None or self.rightChild is None  ):
            # print("Error: either child is none")
            return
        elif ( self.overflowed <= 0 ):
            print("Error: not overflowed")
        else:
            self.leftChild.fillLiquid( self.overflowed / 2 )
            self.rightChild.fillLiquid( self.overflowed / 2 )


















