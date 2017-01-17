class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def helper(s, p, s_index, p_index):
            if s_index == -1 and p_index == -1:
                return True
            if p_index == -1 and s_index != -1:
                return False
            if p_index != -1 and s_index == -1:
                if p_index >= 2 and p[p_index - 1] == "*":
                    return helper(s, p, s_index, p_index - 2)
                else:
                    return False
            
        return helper(s, p, len(s) - 1, len(p) - 1)

sol = Solution()
print sol.isMatch("aa", "a")
