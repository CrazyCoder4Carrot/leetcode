# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        def helper(root):
            queue = [root]
            while queue:
                temp = []
                level = []
                for node in queue:
                    level += [node.val]
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                res.append(level)
                queue = temp
        helper(root)
        return res