import collections
class Solution(object):
    def isAnagram(self, c1, c2):
        counter1 = collections.Counter(c1)
        counter2 = collections.Counter(c2)
        return counter1 == counter2
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        if len(s) == len(p):
            if self.isAnagram(s, p):
                return [0]
        res = []
        length = len(p)
        counter1 = collections.Counter(s[:length])
        counter2 = collections.Counter(p)
        for i in range(len(s) - length + 1):
            if counter1 == counter2:
                res.append(i)
            if i + length < len(s):
                counter1[s[i + length]] += 1
            counter1[s[i]] -= 1
            if counter1[s[i]] == 0:
                del counter1[s[i]]
            
        return res