import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(math.sqrt(area))
        if mid * mid == area:
            return [mid, mid]
        for w in range(mid, -1, -1):
            if area % w == 0:
                return [area / w, w]
