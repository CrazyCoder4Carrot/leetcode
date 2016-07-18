class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a = dividend
        b = divisor
        flag = False
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            flag = True
        a, b = abs(a), abs(b)
        c = b
        mut = 1
        res = 0
        while a > 0 :
            if a >= c:
                res += mut
                a -= c
                c <<= 1
                mut <<= 1
            else:
                c >>= 1
                mut >>= 1
        if flag:
            res = -res
        return min(2147483647, max(-2147483648, res))