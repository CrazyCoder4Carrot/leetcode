# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    cur_max = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.cur_max
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        left = 0 if not left else (left if left > 0 else 0)
        right = 0 if not right else (right if right > 0 else 0)
        self.cur_max = max(left + right + root.val, self.cur_max)
        return max(left, right) + root.val
    