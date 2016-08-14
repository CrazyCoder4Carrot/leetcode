class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxval = minval = res = nums[0]
        for i in range(1, len(nums)):
            temp = maxval
            maxval = max(nums[i], maxval * nums[i], minval * nums[i])
            minval = min(nums[i], temp * nums[i], minval * nums[i])
            res = max(maxval, res)
        return res