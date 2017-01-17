class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, low = 0, 0
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
            count = sum(dict.values()) - max(dict.values())
            while count > k and low <= i:
                dict[s[low]] -= 1
                if dict[s[low]] == 0:
                    del dict[s[low]]
                low += 1
                count = sum(dict.values()) - max(dict.values())
            res = max(res, i - low + 1)
        return res