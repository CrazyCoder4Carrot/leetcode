class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(i, j, rooms, 0)
    def dfs(self, i, j, rooms, distance):
        if i < 0 or j < 0 or j >= len(rooms[0]) or i >= len(rooms) or rooms[i][j] < distance:
            return 0
        rooms[i][j] = min(rooms[i][j], distance)
        self.dfs(i-1,j, rooms, distance + 1)
        self.dfs(i,j-1, rooms, distance + 1)
        self.dfs(i,j+1, rooms, distance + 1)
        self.dfs(i+1,j, rooms, distance + 1)