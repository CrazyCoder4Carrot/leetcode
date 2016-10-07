import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        temp = collections.defaultdict(int)
        oddsumcurve, evensum, oddsum = 0, 0, 0
        for i in s:
            temp[i] += 1
        for value in temp.values():
            if value % 2 == 0:
                evensum += value
            else:
                oddsumcurve += value - 1
                oddsum += value
        if oddsum == 0:
            return evensum
        else:
            return evensum + oddsumcurve + 1