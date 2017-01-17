class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) <= 1:
            return len(s)
        dict1 = {}
        start, end = 0, 0
        substr = ""
        maxval = 0
        for i in range(len(s)):
            if s[i] in dict1 and dict1[s[i]] >= start:
                start = dict1[s[i]] + 1
            end += 1
            maxval = max(maxval, end - start)
            dict1[s[i]] = i
        return maxval