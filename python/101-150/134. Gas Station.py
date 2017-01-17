class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalgas = totalcost = tank = begin = 0
        for i in range(len(gas)):
            totalgas += gas[i]
            totalcost += cost[i]
            tank += (gas[i] - cost[i])
            if tank < 0:
                begin = 1 + i
                tank = 0
        return begin if totalgas >= totalcost else -1