class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        w = [0, k, k*k]
        while len(w) <= n:
            w += [sum(w[-2:]) * (k-1)]
        return w[n]