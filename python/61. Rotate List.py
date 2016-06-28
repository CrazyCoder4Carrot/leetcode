# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        if not head or not head.next:
            return head
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        k = k % length
        if k == 0:
            return head
        end = head
        pre = dummyhead
        while k > 0:
            pre = pre.next
            end = end.next
            k -= 1
        start = head
        while end:
            end = end.next
            pre = pre.next
            start = start.next
        cur = head
        while cur.next:
            if cur.next == start:
                cur.next = None
                break
            cur = cur.next
        pre.next= head
        return start