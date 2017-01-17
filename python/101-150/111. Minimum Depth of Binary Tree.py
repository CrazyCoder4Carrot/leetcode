# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            temp = []
            for node in queue:
                if not node.left and not node.right:
                    return depth + 1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            depth += 1
            queue = temp
        