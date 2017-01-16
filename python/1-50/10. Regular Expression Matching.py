class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def helper(s, p):
            if not p and not s:
                return True
            if not s and p:
                if len(p) > 1 and p[1] == "*":
                    return helper(s, p[2:])
                else:
                    return False
            if not p and s:
                return False
            if p[0] == s[0] or p[0] == ".":
                if len(p) > 1 and p[1] == "*":
                    return helper(s[1:], p) or helper(s, p[2:])
                else:
                    return helper(s[1:], p[1:])
            else:
                if len(p) > 1 and p[1] == "*":
                    return helper(s, p[2:])
                else:
                    return False
        return helper(s, p)


