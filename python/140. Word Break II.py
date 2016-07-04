from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dic = collections.defaultdict(list)
        
        def helper(s):
            if not s:
                return [None]
            if s in dic:
                return dic[s]
            res = []
            for word in wordDict:
                n = len(word)
                if word == s[:n]:
                    for each in helper(s[n:]):
                        if each:
                            res.append(word+" "+each)
                        else: 
                            res.append(word)
                dic[s] = res
            return res
        return helper(s)
            
            