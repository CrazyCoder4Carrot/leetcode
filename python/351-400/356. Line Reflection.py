import sys
import collections


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        pointsDict = collections.defaultdict(bool)
        if not points:
            return True
        minX = sys.maxint
        maxX = -sys.maxint
        for x, y in points:
            minX = min(x, minX)
            maxX = max(x, maxX)
        midy = (minX + maxX) / 2.0

        for x, y in points:
            pointsDict[(x, y)] = True
        for x, y in points:
            newx = 2 * midy - x
            if not pointsDict[(newx, y)]:
                return False
        return True
