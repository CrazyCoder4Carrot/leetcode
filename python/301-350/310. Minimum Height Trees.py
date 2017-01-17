import collections
import sys
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs(root, distance, level):
        	level += 1
        	for node in graph[root]:
        		distance[node] = level
        		visit[node] = True
        		if not visit[node]:
        			dfs(node, distance)
        if not edges:
        	return []
        graph = collections.defaultdict(list)
        for a,b in edges:
        	graph[a].append(b) 
        	graph[b].append(a)
        vetex = set(graph.keys())
        res = []
        while len(vetex) > 2:
        	leaves = [x for x in graph if len(graph[x]) == 1]
        	for x in leaves:
        		for y in graph[x]:
        			graph[y].remove(x)
        		del graph[x]
        		vetex.remove(x)
       	return list(vetex) if n != 1  else [0]
sol = Solution()
print sol.findMinHeightTrees(4,[[1,0],[1,2],[1,3]])