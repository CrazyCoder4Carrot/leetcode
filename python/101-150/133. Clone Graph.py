# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        newnode = UndirectedGraphNode(node.label)
        dic = {}
        dic[node] = newnode
        queue = [node]
        while queue:
            cur = queue.pop(0)
            for n in cur.neighbors:
                if n in dic:
                    dic[cur].neighbors += [dic[n]]
                else:
                    temp = UndirectedGraphNode(n.label)
                    dic[n] = temp
                    dic[cur].neighbors += [temp]
                    queue.append(n)
        return newnode
        