class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    res[i][j] = max(res[i - zeros][j - ones] + 1, res[i][j])
            print res
        return res[-1][-1]
