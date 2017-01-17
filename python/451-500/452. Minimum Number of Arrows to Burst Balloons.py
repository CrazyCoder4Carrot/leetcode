class Solution(object):
    import sys

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[1])
        res = 0
        end = -sys.maxint
        for interval in points:
            if interval[0] < end:
                res += 1
                end = interval[1]
        return res
