class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        total = []
        rownums = [[] for _ in range(9)]
        colnums = [[] for _ in range(9)]
        gridnums = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    total.append((i, j))
                else:
                    temp = board[i][j]
                    rownums[i].append(temp)
                    colnums[j].append(temp)
                    gridnums[i / 3 * 3 + j / 3].append(temp)

        def helper(level, total):
            if len(total) == level:
                return True
            i, j = total[level]
            allcan = map(str, range(1, 10))
            candidiates = list(set(allcan) - set(rownums[i])
                - set(colnums[j]) - set(gridnums[i / 3 * 3 + j/3]))
            if not candidiates:
                return False
            for num in candidiates:
                board[i][j] = str(num)
                rownums[i].append(str(num))
                colnums[j].append(str(num))
                gridnums[i / 3 * 3 + j / 3].append(str(num))
                flag = helper(level + 1, total)
                if not flag:
                    board[i][j] = "."
                    rownums[i].pop()
                    colnums[j].pop()
                    gridnums[i / 3 * 3 + j / 3].pop()
                else:
                    return True
        helper(0, total)
