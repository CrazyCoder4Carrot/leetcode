class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n < 0 or m < 0:
            return 0
        total = m + n - 2
        upper = lower = 1
        for i in range(m - 1):
            upper *= total
            total -= 1
        for i in range(1, m):
            lower *= i
        return upper/lower