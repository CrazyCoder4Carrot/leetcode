import collections
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        temp1 = collections.defaultdict(int)
        temp2 = collections.defaultdict(int)
        for c1, c2 in zip(s1, s2):
            temp1[c1] += 1
            temp2[c2] += 1
        if temp1 != temp2:
            return False
        l1temp = collections.defaultdict(int)
        l2temp = collections.defaultdict(int)
        r2temp = collections.defaultdict(int)
        for i in range(len(s1) - 1):
            l1temp[s1[i]] += 1
            l2temp[s2[i]] += 1
            r2temp[s2[len(s2) - 1 - i]] += 1
            if l1temp == l2temp:
                if self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]):
                    return True
            elif l1temp == r2temp:
                if self.isScramble(s1[:i+1], s2[-(i + 1):]) and self.isScramble(s1[i+1:], s2[:-(i+1)]):
                    return True
        return False
            
            
            
            