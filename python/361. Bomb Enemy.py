import sys
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        column = len(grid[0])
        res = 0 
        cols = [0 for _ in range(column)]
        rows = 0
        for i in range(row):
            for j in range(column):
                if j == 0 or grid[i][j-1] =="W":
                    rows = 0
                    for k in range(j, column):
                        if grid[i][k] == "W":
                            break
                        if grid[i][k] == "E":
                            rows += 1
                if i == 0 or grid[i-1][j] == "W":
                    cols[j] = 0
                    for k in range(i, row):
                        if grid[k][j] == "W":
                            break
                        if grid[k][j] == "E":
                            cols[j] += 1
                if grid[i][j] == "0":
                    res = max(res, rows + cols[j])
        return res
                    
        