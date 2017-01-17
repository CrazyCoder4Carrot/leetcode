class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        res = []
        for num in nums:
            res.append(a*num * num + b * num + c)
        return sorted(res)