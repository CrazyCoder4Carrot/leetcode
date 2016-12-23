class Solution(object):

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.res = []
        self.count = 0

        def helper(path, i, j):
            if i < 0 or j < 0 or i >= 3 or j >= 3 or len(path) > n or keyboard[i][j] in path:
                return
            print path,i ,j
            if len(path) >= m:
                if path not in self.res:
                    self.res.append(path)
                    self.count += 1
            helper(path + [keyboard[i][j]], i+1, j)
            helper(path + [keyboard[i][j]], i-1, j)
            helper(path + [keyboard[i][j]], i, j+1)
            helper(path + [keyboard[i][j]], i, j-1)
            helper(path + [keyboard[i][j]], i+1, j+1)
            helper(path + [keyboard[i][j]], i+1, j-1)
            helper(path + [keyboard[i][j]], i-1, j+1)
            helper(path + [keyboard[i][j]], i-1, j-1)
            helper(path + [keyboard[i][j]], i+1, j+2)
            helper(path + [keyboard[i][j]], i+1, j-2)
            helper(path + [keyboard[i][j]], i-1, j-2)
            helper(path + [keyboard[i][j]], i-1, j+2)
        for i in range(len(keyboard)):
            for j in range(len(keyboard[0])):
                helper([], i, j)
        return self.count


sol = Solution()
sol.numberOfPatterns(1,2)
print sol.count
print sol.res
