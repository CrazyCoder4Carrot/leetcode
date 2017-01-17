class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2:
            return size
        delta = nums[1] - nums[0]
        ans = 1 + (delta != 0)
        for x in range(2, size):
            newDelta = nums[x] - nums[x-1]
            if newDelta * delta < 0:
                ans += 1
                delta = newDelta
        return ans