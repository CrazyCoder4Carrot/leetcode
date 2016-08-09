class Solution(object):
    def isAdditiveNumber(self, num, i = 0, n = 1, pre2 = None, pre1 = None):
        """
        :type num: str
        :rtype: bool
        """
        if i == len(num):
            return n > 3
        for size in range(1, len(num) - i + 1):
            if size > 1 and num[i] == "0":
                return False
            v = int(num[i:i+size])
            if n > 2 and v != pre2 + pre1:
                continue
            if self.isAdditiveNumber(num, i + size, n + 1, pre1, v):
                return True
        return False
                