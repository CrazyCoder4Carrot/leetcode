class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        flags1 = [[0] * n for _ in range(m)]
        flags2 = [[0] * n for _ in range(m)]

        def helper(i, j, m, n, flags):
            flags[i][j] = True
            indexarr = [0, 1, 0, -1, 0]
            for k in range(len(indexarr) - 1):
                x = i + indexarr[k]
                y = j + indexarr[k + 1]
                print x, y, m, n
                if x < 0 or y < 0 or x >= m or y >= n or flags[x][y] or matrix[i][j] > matrix[x][y]:
                    continue
                helper(x, y, m, n, flags)
        for j in range(n):
            helper(0, j, m, n, flags1)
            helper(m - 1, j, m, n, flags2)
        for i in range(m):
            helper(i, 0, m, n, flags1)
            helper(i, n - 1, m, n, flags2)
        return [[i, j] for i in range(m) for j in range(n) if flags1[i][j] and flags2[i][j]]

sol = Solution()
matrix = [[1,1],[1,1],[1,1]]
sol.pacificAtlantic(matrix)