class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def helper(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            else:
                return grid[i][j]
        total = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    total += 1
                    count += helper(i, j+1) + helper(i, j-1) + helper(i+1, j) + helper(i-1, j)
        return total * 4 - count