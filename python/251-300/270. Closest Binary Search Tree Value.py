# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        diff = sys.maxint
        while root:
            if abs(root.val - target) < diff:
                diff = abs(root.val - target)
                ans = root.val
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return ans