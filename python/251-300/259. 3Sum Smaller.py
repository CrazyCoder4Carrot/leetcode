class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if 3 * nums[i] >= target:
                return res
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] < target:
                    res += end - start
                    start += 1
                else:
                    end -= 1
        return res