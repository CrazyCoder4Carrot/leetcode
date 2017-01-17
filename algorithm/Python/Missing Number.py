class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        expectedsum = (0+count)*(count+1)/2
        inputsum = sum(nums)
        return expectedsum - inputsum

solution = Solution()

nums = [0,1,2,4]

print solution.missingNumber(nums)