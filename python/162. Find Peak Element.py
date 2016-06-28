class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        if len(nums) == 1:
            return 0
        while start < end:
            mid = (start + end) / 2
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start
        