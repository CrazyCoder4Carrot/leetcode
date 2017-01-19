class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        temp = num
        while num:
            cnt += 1
            num >>= 1
        return 2 ** cnt - 1 - temp