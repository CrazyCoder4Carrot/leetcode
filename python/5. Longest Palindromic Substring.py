class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s, begin, end):
            while begin >= 0 and end < len(s) and s[begin] == s[end]:
                begin -= 1
                end += 1
            return s[begin+1: end]
        if not s:
            return ""
        if len(s) == 1 or s == s[::-1]:
            return s
        longest = s[0]
        for i in range(len(s)):
            temp = helper(s, i, i)
            if len(temp) > len(longest):
                longest = temp
            temp = helper(s, i , i + 1)
            if len(temp) > len(longest):
                longest = temp
        return longest