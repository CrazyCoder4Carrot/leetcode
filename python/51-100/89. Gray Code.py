class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        mask = 1 <<n 
        res = []
        for i in range(mask):
            res.append(i ^ i >> 1)
        return res