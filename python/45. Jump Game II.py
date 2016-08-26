class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0
        start, end, step, maxdis = 0, nums[0], 1, nums[0]
        while end < len(nums) - 1:
            for i in range(start + 1, end + 1):
                maxdis = max(maxdis, nums[i] + i)
            start = end
            end = maxdis
            step += 1
        return step
        