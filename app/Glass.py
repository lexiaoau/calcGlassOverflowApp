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
      # self.isFull = False

      # self.outMost = False

      # if( self.leftParent is None or self.rightParent is None ):
      #   self.outMost = True


    def fillLiquid(self, amount):
        self.filled = self.filled + amount
        if( self.filled > self.capacity ):
            self.overflowed = self.filled - self.capacity
            self.filled = self.capacity
            # self.isFull = True

















