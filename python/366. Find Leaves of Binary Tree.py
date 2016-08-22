# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node):
            if not node:
                return -1
            i = 1 + max(dfs(node.left), dfs(node.right))
            if i == len(out):
                out.append([])
            out[i].append(node.val)
            return i
        out = []
        dfs(root)
        return out
        