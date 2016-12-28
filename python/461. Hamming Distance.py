class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = x ^ y
        count = 0
        while res:
            count += 1 if res & 1 else 0
            res >>= 1
        return count
