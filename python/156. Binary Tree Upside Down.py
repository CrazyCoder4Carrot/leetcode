# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        l = self.upsideDownBinaryTree(root.left)
        r = l
        while r.right:
            r = r.right
        root, r.left, r.right = l, root.right, TreeNode(root.val)
        return root