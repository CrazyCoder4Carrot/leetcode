class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                if c == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        level = {s}
        while True:
            temp = []
            valid = filter(isvalid, level)
            if valid:
                return valid
            for str in level:
                for i in range(len(str)):
                    temp.append(str[:i] + str[i + 1:])
            level = list(set(temp))