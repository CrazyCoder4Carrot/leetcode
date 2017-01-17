class Solution(object):

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = n = 0
        count = 0
        for i in range(32):
            m = n = 0
            for num in nums:
                if num & (1 << i):
                    m += 1
                else:
                    n += 1
            count += m * n
        return count
