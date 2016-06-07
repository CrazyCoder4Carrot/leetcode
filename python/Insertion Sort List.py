# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummyhead = ListNode(-1)
        dummyhead.next = None
        node = head
        while node:
            pre = dummyhead
            cur = dummyhead.next
            while cur and cur.val < node.val:
                pre = cur
                cur = cur.next
            pre.next = node
            temp = node.next
            node.next = cur
            node = temp
        return dummyhead.next
                