class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        island = Union()
        for p in map(tuple, positions):
            island.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in island.id:
                    island.union(p, q)
            res += [island.count]
        return res


class Union(object):
    def __init__(self):
        self.id = {}
        self.size = {}
        self.count = 0

    def add(self, i):
        self.id[i] = i
        self.size[i] = 1
        self.count += 1

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def union(self, i, j):
        root1, root2 = self.root(i), self.root(j)
        if root1 == root2:
            return
        if self.size[root1] > self.size[root2]:
            root1, root2 = root2, root1
        self.id[root1] = root2
        self.size[root2] += self.size[root1]
        self.count -= 1
