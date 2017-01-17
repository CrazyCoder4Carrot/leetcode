class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = [[0 for _ in range( n + 1)] for _ in range(m+1)]
        res[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not grid[i-1][j-1]:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]