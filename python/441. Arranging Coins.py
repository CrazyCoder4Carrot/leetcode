import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        bound = int(math.sqrt(n*2))
        i = bound
        while (1+i)*i/2 > n:
            i -=1
        return i
        