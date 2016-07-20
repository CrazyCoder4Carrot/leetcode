class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if not n or not m:
            return
        for i in range(m):
            for j in range(n):
                count = sum([board[ii][jj]%2 for ii in range(i-1, i + 2) for jj in range(j-1, j + 2) if 0 <= ii < m and 0 <= jj < n]) - board[i][j]
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0