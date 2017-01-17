# Definition for a binary tree node.

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(s, e):
            res = []
            if s > e:
                res.append(None)
                return res
            if s == e:
                res.append(TreeNode(s))
                return res
            for i in range(s, e + 1):
                left = helper(s, i - 1)
                right = helper(i + 1, e)
                for leftnode in left:
                    for rightnode in right:
                        root = TreeNode(i)
                        root.left = leftnode
                        root.right = rightnode
                        res.append(root)
            return res
        return helper(1, n)


