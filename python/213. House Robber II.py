class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        res = [0] * (len(nums) - 1)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            res[i] = max(nums[i] + res[i-2], res[i-1])
        res1 = res[-1]
        res = [0] * (len(nums) - 1)
        res[0] = nums[1]
        res[1] = max(nums[2], nums[1])
        for i in range(2, len(nums) - 1):
            res[i] = max(nums[i+1] + res[i-2], res[i-1])
        res2 = res[-1]
        return max(res1, res2)