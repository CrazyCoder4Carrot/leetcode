# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        end = len(lists) - 1
        while end > 0:
            start = 0
            while start < end:
                lists[start] = self.merge(lists[start], lists[end])
                start += 1
                end -= 1
        return lists[0]
    def merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        head = ListNode(0)
        cur = head
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        cur.next = a or b
        return head.next