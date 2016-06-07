# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root)
    def helper(self, root):
        if not root:
            return 0
        r = l = root
        llevel = rlevel = 0
        while l:
            llevel += 1
            l = l.left
        while r:
            rlevel += 1
            r = r.right
        if llevel == rlevel:
            return 2 ** llevel - 1
        return self.helper(root.left) + self.helper(root.right) + 1