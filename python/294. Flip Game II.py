class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.memo = {}
        return self.helper(s)
    def helper(self, s):
        if s not in self.memo:
            if "++" not in s:
                return False
            res = []
            for i in range(len(s) - 1):
                if s[i:i+2] == "++":
                    temp = s[:i] + "--" + s[i+2:]
                    res.append(self.helper(temp))
            self.memo[s] = not all(res)
        return self.memo[s]
                
            
        
        