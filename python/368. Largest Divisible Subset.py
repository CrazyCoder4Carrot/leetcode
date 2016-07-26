class Solution(object):
    def largestDivisibleSubset(self, nums):
        S = {-1: list()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) + [x]
        return max(S.values(), key=len)