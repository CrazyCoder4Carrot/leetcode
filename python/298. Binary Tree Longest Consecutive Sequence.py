# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 1
        if not root:
            return 0
        def helper(root, val):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            count = 0 
            if root.val -1 == val :
                count += 1
            return max(helper(root.left, root.val), count, helper(root.right, root.val))
        return self.max
                
                
                