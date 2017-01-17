class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        sell = [0] * len(prices)
        cooldown = [0] * len(prices)
        sell[1] = prices[1] - prices[0]
        for i in range(2, len(prices)):
            cooldown[i] = max(sell[i-1], cooldown[i-1])
            sell[i] = prices[i] - prices[i-1] + max(sell[i-1], cooldown[i-2])
        return max(sell[-1], cooldown[-1])