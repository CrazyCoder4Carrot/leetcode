class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == "O":
                    queue.append((i,j))
        while queue:
            x, y = queue.pop(0)
            board[x][y] = "V"
            if x -1 >= 0 and board[x-1][y] == "O":
                queue.append((x-1, y))
            if x + 1 < m and board[x+1][y] == "O":
                queue.append((x+1, y))
            if y - 1 >= 0 and board[x][y-1] == "O":
                queue.append((x, y - 1))
            if y + 1 < n  and board[x][y+1] == "O":
                queue.append((x, y + 1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "V":
                    board[i][j] = "O"
        