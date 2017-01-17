class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        while l < r:
            for i in range(m):
                matrix[l][i], matrix[r][i] = matrix[r][i], matrix[l][i]
            l += 1
            r -= 1
        for i in range(n):
            for j in range(i + 1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        