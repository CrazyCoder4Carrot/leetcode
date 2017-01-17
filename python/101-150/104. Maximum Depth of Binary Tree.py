# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, depth):
            if not root:
                return depth
            return max(helper(root.left, depth + 1), helper(root.right, depth + 1))
        return helper(root, 0)