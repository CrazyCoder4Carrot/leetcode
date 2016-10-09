class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length = max(len(num1), len(num2))
        res = [0] * length 
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        k = length - 1
        while k >= 0 and j >= 0 and i >= 0:
            res[k] = int(num1[i]) + int(num2[j]) + carry
            j -= 1
            i -= 1
            if res[k] >= 10:
                res[k] = res[k] % 10
                carry = 1
            else:
                carry = 0
            k -= 1
        while j >= 0:
            res[k] = int(num2[j]) + carry
            j -= 1
            if res[k] >= 10:
                res[k] = res[k] % 10
                carry = 1
            else:
                carry = 0
            k -= 1
        while i >= 0:
            res[k] = int(num1[i]) + carry
            i -= 1
            if res[k] >= 10:
                res[k] = res[k] % 10
                carry = 1
            else:
                carry = 0
            k -= 1          
        if carry :
            res = [1] + res
        res = "".join(map(str, res))
        return res