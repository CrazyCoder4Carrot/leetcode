# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxval = 1
        if not root:
            return 0

        def dfs(root, isleft):
            if not root:
                return 0, 0, sys.maxint, -sys.maxint
            lsize, lcnt, lmin, lmax = dfs(root.left)
            rsize, rcnt, rmin, rmax = dfs(root.right)
            n = lcnt + rcnt + 1 if lmax < root.val < rmin else -sys.maxint
            return max(lsize, rsize, n), n, min(lmin, root.val), max(rmax, root.val)
        dfs(root)[0]
        return self.maxval
