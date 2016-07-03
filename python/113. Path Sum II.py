# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, sum, [], res)
        return res
    def dfs(self, root, sum, path, res):
        if not root:
            return
        if sum == root.val and not root.left and not root.right:
            path += [root.val]
            res.append(path)
        if root.left:
            self.dfs(root.left, sum-root.val, path + [root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, path + [root.val], res)