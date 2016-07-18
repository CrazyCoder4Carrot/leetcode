class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.helper(nums, target)
        if left < len(nums) and nums[left] == target:
            right = self.helper(nums, target + 1) - 1
            return [left, right]
        return [-1, -1]
    def helper(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) / 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return r