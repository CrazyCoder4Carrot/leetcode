class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i >= 0 and nums[i] <= nums[i-1]:
            i -= 1
        nums[i:] = reversed(nums[i:])
        if i > 0:
            k = i 
            pivot = nums[i-1]
            while k < len(nums) and nums[k] <= pivot:
                k += 1
            nums[k], nums[i-1] = nums[i-1], nums[k]