class Solution(object):
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def helper(s, p):
            print s, p
            if not s and not p:
                return True
            if s and not p:
                return False
            if not s and p:
                if len(p) >= 2 and p[1] == "*":
                    return helper(s, p[2:])
                else:
                    return False
            if p[0] == s[0] or p[0] == ".":
                if len(p) >= 2 and p[1] == "*":
                    return helper(s[1:], p[2:]) or helper(s[1:], p)
                else:
                    return helper(s[1:], p[1:])
            if s[0] != p[0]:
                if len(p) >= 2 and p[1] == "*":
                    return helper(s, p[2:])
                else:
                    return False
                    
        return helper(s, p)
            
            
sol = Solution()
print sol.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c")