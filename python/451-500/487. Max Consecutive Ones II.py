class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = low = zeros = 0
        k = 1
        for high in range(len(nums)):
            if nums[high] == 0:
                zeros += 1
            while zeros > k:
                if nums[low] == 0:
                    zeros -= 1
                low += 1
            res = max(res, high - low + 1)
        return res


sol = Solution()
nums = [1, 0, 1, 1, 0, 1]
print sol.findMaxConsecutiveOnes(nums)
