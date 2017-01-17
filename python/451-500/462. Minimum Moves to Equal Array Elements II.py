class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = nums[len(nums)/2]
        res = 0
        for i in range(len(nums)):
            res += abs(nums[i]-mid)
        return res