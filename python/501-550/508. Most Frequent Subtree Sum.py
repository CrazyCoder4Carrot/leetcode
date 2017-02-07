# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        sum_dic = collections.defaultdict(int)
        def helper(root):
            if not root:
                return 0
            sumval = helper(root.left) + helper(root.right) + root.val
            sum_dic[sumval] += 1
            return sumval
        res = []
        helper(root)
        fre_max = max(sum_dic.values())
        for key in sum_dic:
            if sum_dic[key] == fre_max:
                res.append(key)
        return res
