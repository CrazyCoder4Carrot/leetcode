class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = [[0]* (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        maxsize = 0
        for i in range(1, len(res)):
            for j in range(1, len(res[0])):
                if matrix[i-1][j-1] == "1":
                    res[i][j] = 1 + min(res[i-1][j], res[i-1][j-1], res[i][j-1])
                    maxsize = max(maxsize, res[i][j])
                else:
                    res[i][j] = 0
        return maxsize * maxsize