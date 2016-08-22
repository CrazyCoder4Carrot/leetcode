class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return all(num[i] + num[~i] in "696 00 11 88" for i in range(len(num)))
        