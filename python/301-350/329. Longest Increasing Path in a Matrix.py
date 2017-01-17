class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1,j) if i and val > matrix[i-1][j] else 0,
                    dfs(i+1,j) if i+1 < len(matrix) and val > matrix[i+1][j] else 0,
                    dfs(i, j - 1) if j-1 >= 0 and val > matrix[i][j-1] else 0,
                    dfs(i, j + 1) if j + 1 < len(matrix[0]) and val > matrix[i][j+1] else 0)
            return dp[i][j]
        if not matrix :
            return 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        return max(dfs(x,y) for x in range(len(matrix)) for y in range(len(matrix[0])))