# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, depth, left):
            if not root:
                return 0, 0
            if not root.left and not root.right:
                return root.val, depth
            lval, ldepth = helper(root.left, depth + 1)
            if not root.right:
                return lval, ldepth
            else:
                rval, rdepth = helper(root.right.left, depth + 2)
                if ldepth > rdepth:
                    return lval, ldepth
                else:
                    return rval, rdepth
        return helper(root, 0)[0]
