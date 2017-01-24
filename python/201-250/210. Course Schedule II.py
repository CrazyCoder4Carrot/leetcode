import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        firstlevel = [True] * numCourses
        for pair in prerequisites:
            firstlevel[pair[0]] = False
            graph[pair[1]].append(pair[0])
        visited = collections.defaultdict(bool)
        stack = []
        def dfs(cur):
            if len(graph[cur]) == 0:
                stack.append(cur)
                return 
            for node in graph[cur]:
                print node
                if not visited[node]:
                    visited[node] = True
                    dfs(node)
            stack.append(cur)
        for i in range(numCourses):
            if firstlevel[i]:
                visited[i] = True
                dfs(i)
        return stack[::-1]

sol = Solution()
num = 4
pre = [[1,0],[2,1],[3,2],[1,3]]
print sol.findOrder(num, pre)