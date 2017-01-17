import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for x, y in points:
            distance_dict = collections.defaultdict(int)
            for p, q in points:
                distance = (y-q)**2 + (x-p)**2
                distance_dict[distance] += 1
            for val in distance_dict.values():
                res += val*(val-1)
        return res
        