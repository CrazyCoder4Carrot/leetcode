class Solution(object):
    import sys
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = sys.maxint
        houses.sort()
        heaters.sort()
        heaters += [sys.maxint]
        r = i = 0
        for x in houses:
            while x >= sum(heaters[i:i + 2]) / 2.0:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r
