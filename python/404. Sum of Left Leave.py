# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root, False)
        return res
    def helper(self, root, left):
        if not root:
            return 0
        if left and not root.left and not root.right:
            return root.val
        else:
            return self.helper(root.left, True) + self.helper(root.right, False)