import sys


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        if k >= len(prices) / 2:
            profit = 0
            for i in range(1, len(prices)):
                gap = prices[i] - prices[i - 1]
                if gap > 0:
                    profit += gap
            return profit
        holds = [-sys.maxint] * k
        release = [0] * k
        for price in prices:
            for i in range(k - 1, -1, -1):
                release[i] = max(release[i], holds[i] + price)
                    holds[i] = max(holds[i], -price)
                else:
                    holds[i] = max(holds[i], release[i - 1] - price)
        return release[-1]
