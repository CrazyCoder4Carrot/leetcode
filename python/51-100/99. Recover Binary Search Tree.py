# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(-sys.maxint)
        self.validate(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    def validate(self, root):
        if not root:
            return
        self.validate(root.left)
        if not self.first and self.prev.val >= root.val:
            self.first = self.prev
        if self.first and self.prev.val >= root.val:
            self.second = root
        self.prev = root
        self.validate(root.right)
        
        