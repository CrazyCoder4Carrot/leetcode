"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        vals = []
        self.visit(root, vals)
        if not vals or len(vals) == 1:
            return True
        for i in range(0, (len(vals) - 1)):
            if vals[i] >= vals[i + 1]:
                return False
        return True
    def visit(self, root, nodevals):
        if not root:
            return
        if root.left:
            self.visit(root.left, nodevals)
        nodevals.append(root.val)
        if root.right:
            self.visit(root.right, nodevals)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -sys.maxint, sys.maxint)
    def helper(self, root, minval, maxval):
        if not root:
            return True
        if root.val < maxval and root.val > minval and self.helper(root.left, minval, root.val) and self.helper(root.right, root.val, maxval):
            return True
            
        return False