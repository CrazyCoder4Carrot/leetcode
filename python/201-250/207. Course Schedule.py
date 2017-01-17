import collections
class Solution(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for a, b in prerequisites:
            if a in graph and b not in graph[a]:
                graph[a].append(b)
            else:
                graph[a] = [b]
        remove_list = [i for i in range(n) if i not in graph] 
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
        return len([key for key in graph]) == 0


sol = Solution()
sol.canFinish(2, [[1,0]])