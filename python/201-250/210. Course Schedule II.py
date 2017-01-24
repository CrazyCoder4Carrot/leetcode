import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dic = collections.defaultdict(list)
        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            dic[i].append(j)
            graph[j].append(i)
        stack = [i for i in xrange(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in graph[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            del dic[node]
        return res if not dic else []





sol = Solution()
num = 2
pre = [[1, 0]]
print sol.findOrder(num, pre)
