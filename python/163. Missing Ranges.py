import sys
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(len(nums) - 1):
            gap = nums[i+1] - nums[i]
            if gap != 1:
                if gap == 2:
                    res.append(str(nums[i] + 1))
                else:
                    res.append(str(nums[i] + 1) + "->" + str(nums[i+1] - 1))
        return res
                    
                
            
            