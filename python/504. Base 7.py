class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"
        flag = False
        if num < 0:
            flag = True
            num = -num
        res = ""
        while num:
            res = str(num % 7) + res
            num /= 7
        if flag:
            res = "-" + res
        return res