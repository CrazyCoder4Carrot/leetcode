# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummyhead = ListNode(0)
        dummyhead.next = head
        pre = dummyhead
        cur = pre.next
        next = cur.next
        while pre and cur and next:
            if cur.val == next.val:
                while next and cur.val == next.val:
                    next = next.next
                pre.next = next
                cur = next
                if next:
                    next = next.next
            else:
                pre = cur
                cur = next
                next = next.next
        return dummyhead.next