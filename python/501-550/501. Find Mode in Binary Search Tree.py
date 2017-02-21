# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        fre_dic = collections.defaultdict(int)
        def helper(root):
            fre_dic[root.val] += 1
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
        helper(root)
        maxval = max(fre_dic.values())
        res = []
        for key in fre_dic:
            if fre_dic[key] == maxval:
                res.append(key)
        return res
