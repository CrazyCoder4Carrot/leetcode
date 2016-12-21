class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, index, temp, res):
        if index == 4:
            if not s:
                res.append(".".join(temp))
            return
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], index + 1, temp + [s[:i]], res)
                if s[0] == "0":
                    break
