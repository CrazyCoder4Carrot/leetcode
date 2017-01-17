class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for num in nums:
                if num <= i :
                    dp[i] += dp[i-num]
        print dp
        return dp[target]