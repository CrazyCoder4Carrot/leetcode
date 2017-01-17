class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = b = ret = 0
        for num in nums:
            ret ^= num
        mask = ret & ~(ret-1)
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a,b]
        