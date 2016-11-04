class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        low = 0
        high = x
        while True:
            mid = (low + high) / 2
            if mid * mid > x:
                high = mid - 1
            else:
                if (mid + 1) ** 2 > x:
                    return mid
                low = mid + 1
            