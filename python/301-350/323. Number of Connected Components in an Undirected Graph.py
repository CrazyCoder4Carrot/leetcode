class Solution(object):
    def union(self, unionset ,edge):
        a, b = edge
        #print a, b, unionset
        roota = self.find(unionset, a)
        rootb = self.find(unionset, b)
        if roota == rootb:
            return
        if unionset[roota] < unionset[rootb]:
            if unionset[rootb] < -1:
                for i in range(len(unionset)):
                    if unionset[i] == rootb or i == rootb:
                        unionset[i] = roota
                        unionset[roota] -= 1
            else:
                unionset[rootb] = roota
                unionset[roota] -= 1
        else:
            if unionset[roota] < -1:
                #print a, b, unionset
                for i in range(len(unionset)):
                    if unionset[i] == roota or i == roota:
                        unionset[i] = rootb
                        unionset[rootb] -= 1
            else:
                unionset[roota] = rootb
                unionset[rootb] -= 1
    def find(self, unionset, element):
        if unionset[element] < 0:
            return element
        if unionset[element] >= 0:
            return self.find(unionset, unionset[element])
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        unionset = [-1] * n
        for edge in edges:
            self.union(unionset, edge)
        count = 0
        for val in unionset:
            if val < 0:
                count += 1
        print unionset
        return count