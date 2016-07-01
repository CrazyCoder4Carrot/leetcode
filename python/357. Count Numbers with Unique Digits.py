class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res = 10
        base = 9
        i = 2
        while i <= n and i <= 10:
            base *= (9 - i + 2)
            res += base 
            i += 1
        return res