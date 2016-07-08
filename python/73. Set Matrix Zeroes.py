class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = [0] * len(matrix)
        col = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = col[j] = 1
        for i in range(len(row)):
            if row[i] == 1:
                for j in range(len(col)):
                    matrix[i][j] = 0
        for i in range(len(col)):
            if col[i] == 1:
                for j in range(len(row)):
                    matrix[j][i] = 0
        