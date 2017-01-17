class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(s, [], res)
        return res
    def helper(self, s, temp, res):
        if not s:
            res.append(temp)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.helper(s[i:], temp + [s[:i]], res)
    def isPal(self, s):
        return s == s[::-1]