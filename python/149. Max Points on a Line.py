# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import sys
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        result = 0
        for i in range(len(points)):
            d = {}
            overlap, curmax = 0, 0
            for j in range(i + 1, len(points)):
                dx, dy = points[j].x - points[i].x, points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                slope = dy * 1.0 / dx if dx != 0 else sys.maxint
                if slope in d:
                    d[slope] += 1
                else:
                    d[slope] = 1
                curmax = max(curmax, d[slope])
            result = max(result, curmax + overlap + 1)
        return result
                
                
                
                
                