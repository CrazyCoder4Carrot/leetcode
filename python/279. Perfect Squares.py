import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ub = int(math.sqrt(n))
        for i in range(ub + 1):
            for j in range(i, ub + 1):
                if n >= i * i + j * j:
                    c = int(math.sqrt(n - i * i - j * j))
                    if i * i + j * j + c * c == n:
                        return len(filter(lambda x : x is True, [not not i, not not j, not not c]))
        return 4