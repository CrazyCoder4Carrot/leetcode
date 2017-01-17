class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def tailzero(n):
            cnt = 0
            while (n % 2) == 0:
                print n
                cnt += 1
                n = n >> 1
            return cnt
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n / 2) + 1
        if n == 3:
            return 2
        a = tailzero(n + 1)
        b = tailzero(n - 1)
        print n
        if a > b:
            return self.integerReplacement(n + 1) + 1
        else:
            return self.integerReplacement(n - 1) + 1


sol = Solution()
sol.integerReplacement(7)
