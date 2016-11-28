import collections
class Solution(object):
    def findOrder(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        res = []
        for a, b in prerequisites:
            if a in graph and b not in graph[a]:
                graph[a].append(b)
            else:
                graph[a] = [b]
        remove_list = [i for i in range(n) if i not in graph] 
        res += remove_list
        while remove_list:
            cur_list = [key for key in graph]
            temp = []
            for i in remove_list:
                for key in graph:
                    if i in graph[key]:
                        graph[key].remove(i)
                        if not graph[key]:
                            temp.append(key)
                for key in temp:
                    if key in graph:
                        del graph[key]
            remove_list = [i for i in cur_list if i not in graph]
            res += remove_list
        return res if not graph else []
sol = Solution()
sol.findOrder(2, [[1,0]])