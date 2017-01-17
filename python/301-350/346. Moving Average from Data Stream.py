class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.stack = []
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.stack) == self.size:
            self.stack.pop(0)
        self.stack.append(val)
        return float( float(sum(self.stack))/float(len(self.stack)))