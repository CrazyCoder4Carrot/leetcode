# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        def helper(root, sum):
            if not root:
                return False
            if not root.left and not root.right and sum == root.val:
                return True
            return helper(root.left, sum-root.val) or helper(root.right, sum-root.val)
        return helper(root, sum)