import collections
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        temp = collections.Counter(t)
        for c in s:
            temp[c] -= 1
        for k in temp:
            if temp[k] != 0:
                return k