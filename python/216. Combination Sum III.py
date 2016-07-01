class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.helper(k, n, 1)
    
    def helper(self, k, n, start):
        res = []
        for i in range(start, 10):
            if i > n / k:
                return res
            if k == 1:
                if i == n:
                    return [[i]]
                else:
                    continue
            for c in self.helper(k-1, n-i, i + 1):
                res.append([i] + c)
        return res