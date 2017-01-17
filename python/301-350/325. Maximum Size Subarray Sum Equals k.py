class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        temp = {0:-1}
        subsum = 0
        res = 0
        for i in range(len(nums)):
            subsum += nums[i]
            if subsum not in temp:
                temp[subsum] = i
            if subsum - k in temp:
               res = max(res, i - temp[subsum - k]) 
        return res