class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0
        for i in range(32):
            m <<= 1
            m |= n & 1
            n >>= 1
        return m
