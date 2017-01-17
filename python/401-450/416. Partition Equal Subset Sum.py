class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort(reverse = True)
        def helper(start, target):
            if target < 0 :
                return False
            if target == 0:
                return True
            for i in range(start, len(nums)):
                if helper(i + 1, target - nums[i]):
                    return True
            return False
        sumval = sum(nums)
        return False if sumval % 2 != 0 else helper(0, sumval/2)