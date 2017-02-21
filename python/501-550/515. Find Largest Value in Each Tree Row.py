# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        level = [root]
        while level:
            rowmax = -sys.maxint
            temp = []
            for node in level:
                if node.val > rowmax:
                    rowmax = node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
            res.append(rowmax)
        return res
