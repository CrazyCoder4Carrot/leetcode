class Solution(object):

    def checkcol(self, row, col, path):
        for i in range(row):
            if (i, col) in path:
                return False
        return True

    def checkdig(self, row, col, path):
        for j in range(1, row + 1):
            if (row - j, col + j) in path or (row - j, col - j) in path:
                return False
        return True

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.path = {}
        self.res = 0
        def helper(row, n):
            if len(self.path) == n:
                self.res += 1
                return
            for col in range(n):
                if self.checkcol(row, col, self.path) and self.checkdig(row, col, self.path):
                    self.path[(row, col)] = True
                    helper(row + 1, n)
                    del self.path[(row, col)]

        helper(0, n)
        return self.res
sol = Solution()
print sol.totalNQueens(8)
