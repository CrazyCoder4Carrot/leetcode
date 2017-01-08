class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        res = 0
        i = 0
        start = 0
        while i < len(s):
            if s[i] not in dict:
                dict[s[i]] = i
                res = max(len(dict), res)
            else:
                temp = dict[s[i]]
                for index in range(start, temp + 1):
                    del dict[s[index]]
                start = temp + 1
                dict[s[i]] = i
            i += 1
        return res


sol = Solution()
sol.lengthOfLongestSubstring("abcabcbb")
