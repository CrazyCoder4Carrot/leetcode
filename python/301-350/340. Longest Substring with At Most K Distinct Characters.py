class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        dict = {}
        res = 0
        while j < len(s):
            if s[j] not in dict:
                dict[s[j]] = 1
            else:
                dict[s[j]] += 1
            while i <= j and len(dict) > k:
                dict[s[i]] -= 1
                if dict[s[i]] == 0:
                    del dict[s[i]]
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res