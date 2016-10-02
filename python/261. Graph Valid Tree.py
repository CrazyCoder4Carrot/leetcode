class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges:
            if n >= 2:
                return False
            else:
                return True
        unionset = range(n)
        for edge in edges:
            if not self.union(unionset, edge):
                return False
        root = self.find(unionset, edges[0][0])
        return len(edges) == n-1
        
    def find(self, unionset, v):
        if unionset[v] == v:
            return v
        else:
            unionset[v] = self.find(unionset, unionset[v])
            return unionset[v]
    def union(self, unionset, edge):
        x, y = edge
        rootx, rooty = self.find(unionset, x), self.find(unionset, y)
        #print unionset
        if rootx == rooty:
            return False
        else:
            unionset[rooty] = rootx
        return True