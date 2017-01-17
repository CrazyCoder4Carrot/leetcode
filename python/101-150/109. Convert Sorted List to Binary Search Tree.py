# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        temp = []
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        return self.helper(0, len(temp) - 1, temp)
    def helper(self, low, hi, sortedList):
        if low > hi:
            return None
        mid = (hi - low)/2  + low
        root = TreeNode(sortedList[mid])
        root.left = self.helper(low, mid - 1, sortedList)
        root.right = self.helper(mid + 1, hi, sortedList)
        return root
        