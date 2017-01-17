import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(root, target, val):
            if root not in graph:
                return
            if not visit[root]:
                if root == target:
                    self.res = val
                visit[root] = True
                for i in range(len(graph[root])):
                    node = graph[root][i]
                    edge = pathval[root][i]
                    dfs(node, target, val * edge)
        graph = collections.defaultdict(list)
        pathval = collections.defaultdict(list)
        res = []
        for i in range(len(values)):
            a, b = equations[i]
            val = values[i]
            graph[a].append(b)
            pathval[a].append(val)
            graph[b].append(a)
            pathval[b].append(1/val)
        for a, b in queries:
            self.res = -1.0
            visit = collections.defaultdict(bool)
            dfs(a, b, 1)
            res.append(self.res)
        return res