class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res