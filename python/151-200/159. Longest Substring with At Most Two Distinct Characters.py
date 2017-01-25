import collections


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        slow = 0
        fast = 0
        length = 0
        count = 0
        dic = collections.defaultdict(int)
        while fast < len(s):
            dic[s[fast]] += 1
            if dic[s[fast]] == 1:
                count += 1
                while count > 2:
                    dic[s[slow]] -=1
                    if dic[s[slow]] == 0:
                        count -= 1
                    slow += 1
            length = max(length, fast - slow + 1)
            fast += 1
        return length

sol = Solution()
s = "eceba"
print sol.lengthOfLongestSubstringTwoDistinct(s)
