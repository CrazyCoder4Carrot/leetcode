class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        length = len(str)
        for i in range(1, length/2 + 1):
            if length % i == 0:
                temp = str[0:i]
                count = 0
                for j in range(i, len(str), i):
                    if str[j:j+i] != temp:
                        break
                    count += 1
                if count == length / i -1:
                    return True
        return False
                        