import collections
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        temp = collections.defaultdict(int)
        for i in range(len(s)):
            if i + 10 <= len(s):
                temp[s[i:i+10]] += 1
        res = []
        for key in temp:
            if temp[key] > 1:
                res.append(key)
        return res