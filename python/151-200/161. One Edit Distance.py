class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1, l2 = len(s), len(t)
        if s == t or abs(l1 -l2) > 1:
            return False
        if l1 < l2:
            return self.isOneEditDistance(t, s)
        for i in range(l2):
            if s[i] != t[i]:
                return s[i+1:] == t[i:] or s[i+1:] == t[i+1:]
        return True