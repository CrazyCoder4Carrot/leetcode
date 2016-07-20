class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 1, len(nums) - 1
        while l < r:
            mid = (l + r)/2
            count = 0
            for n in nums:
                if n >= l and n <=mid:
                    count += 1
            if count > mid - l + 1:
                r = mid
            else:
                 l =mid + 1
        return r