class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        s.reverse()
        start = 0
        for i in range(len(s)):
            if s[i] ==  " ":
                s[start:i] = reversed(s[start:i])
                start = i + 1
        s[start:] = reversed(s[start:])