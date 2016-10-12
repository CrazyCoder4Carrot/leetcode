class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsofar = maxsum = nums[0]
        for val in nums[1:]:
            maxsofar = max(maxsofar + val, val)
            maxsum = max(maxsum, maxsofar)
        return maxsum