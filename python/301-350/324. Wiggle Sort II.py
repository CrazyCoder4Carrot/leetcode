class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        k = len(nums) - 1
        j = (len(nums)+1)/2 -1
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = temp[j]
                j -= 1
            else:
                nums[i] = temp[k]
                k -= 1
        