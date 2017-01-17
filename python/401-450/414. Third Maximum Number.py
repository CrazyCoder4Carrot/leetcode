import sys
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        else:
            a = b = c = -sys.maxint
            for num in nums:
                if num > a and num > b and num > c:
                    c = b
                    b = a
                    a = num
                    continue
                if num > b and num > c and num < a:
                    c = b
                    b = num
                    continue
                if num > c and num < a and num < b:
                    c = num
                    continue
        return c if c != -sys.maxint else a
                
                    