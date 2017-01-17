class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf")
        sum = head = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res, i - head + 1)
                sum -= nums[head]
                head += 1
        return res if res <= len(nums) else 0
                
        