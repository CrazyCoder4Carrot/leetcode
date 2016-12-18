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

        def isBST(root, isleft):
            if not root:
                return 0, True, -sys.maxint, sys.maxint
            if not root.left and not root.right:
                return 1, True, 
            lcnt, isleft, lmin, lmax = isBST(root.left, True)
            rcnt, isright, rmin, rmax = isBST(root.right, False)
            if root.val > lmin and root.val > rmin and root.val < lmax and root.val < rmax and isleft and isright:
                total = lcnt + rcnt + 1
                self.maxval = max(self.maxval, total)
                print root.val
                return total, True, min(lmin, rmin), max(lmax, rmax)
            else:
                return 1, False, root.val
        isBST(root, False)
        return self.maxval
