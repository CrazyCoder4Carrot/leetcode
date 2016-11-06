# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        def test(root, sum):
            if not root:
                return 0
            if root.val == sum:
                return 1 + test(root.left, sum - root.val) + test(root.right, sum - root.val)
            else:
                if not root.left and not root.right:
                    return 0
                else:
                    return test(root.left, sum - root.val) + test(root.right, sum - root.val)
        def preorder(root, sum):
            if not root:
                return
            if root:
                temp = test(root, sum)
                if temp:
                    self.count += temp
            if root.left:
                preorder(root.left, sum)
            if root.right:
                preorder(root.right, sum)

        preorder(root, sum)
        return self.count

            