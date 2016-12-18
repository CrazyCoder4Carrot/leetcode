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
        def helper(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            rightmax = leftmax = 0
            if root.left:
                leftmax = helper(root.left)
                if root.val == root.left.val - 1:
                    leftmax += 1
                else:
                    self.max = max(self.max, leftmax)
                    leftmax = 1
            if root.right:
                rightmax = helper(root.right)
                if root.val == root.right.val - 1:
                    rightmax += 1
                else:
                    self.max = max(self.max, rightmax)
                    rightmax = 1
            self.max = max(self.max, leftmax, rightmax)
            return max(rightmax, leftmax)
        helper(root)
        return self.max
                
                
                