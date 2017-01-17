class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        stack = []
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    stack = [(i, j)]
                    while stack:
                        x,y = stack.pop(0)
                        grid[x][y] = "0"
                        if x - 1 >=0 and grid[x-1][y] == "1":
                            grid[x-1][y] = "0"
                            stack.append((x - 1, y))
                        if x + 1 < len(grid) and grid[x+1][y] == "1":
                            grid[x+1][y] = "0"
                            stack.append((x + 1, y))
                        if y-1 >= 0 and grid[x][y-1] == "1":
                            grid[x][y-1] = "0"
                            stack.append((x, y - 1))
                        if y + 1 < len(grid[0]) and grid[x][y+1] == "1":
                            grid[x][y+1] = "0"
                            stack.append((x, y + 1))
                    res += 1
        return res
            