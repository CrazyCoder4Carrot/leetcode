# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, val):
            if not root:
                return 0, True
            if not root.left and not root.right:
                return 1, True
            leftcnt, isleft = helper(root.left, root.val)
            rightcnt, isright = helper(root.right, root.val)
            leftval = root.val if not root.left else root.left.val
            rightval = root.val if not root.right else root.right.val
            if leftval == root.val and rightval == root.val and isleft and isright:
                return leftcnt + rightcnt + 1, True
            else:
                return leftcnt + rightcnt, False
        
        return helper(root, sys.maxint)[0]
        