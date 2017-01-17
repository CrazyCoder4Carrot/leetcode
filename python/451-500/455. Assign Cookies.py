class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i = j = 0
        g.sort()
        s.sort()
        count = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
            else:
                g[i] > s[j]
                j+= 1
        return i
                
                