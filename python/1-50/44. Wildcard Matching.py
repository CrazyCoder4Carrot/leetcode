class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        newp = ""
        for i in range(len(p)):
            if p[i] != "*":
                newp += p[i]
            else:
                if len(newp) >= 1 and newp[-1] == "*":
                    continue
                else:
                    newp += p[i]
        p = newp
        if not s and not p:
            return True
        res = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        res[0][0] = True
        if p and p[0] == "*":
            res[0][1] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    res[i][j] = res[i - 1][j - 1]
                else:
                    if p[j - 1] == "*":
                        res[i][j] = res[
                            i - 1][j] | res[i][j - 1] | res[i - 1][j - 1]
                    else:
                        res[i][j] = False
        return res[-1][-1]
