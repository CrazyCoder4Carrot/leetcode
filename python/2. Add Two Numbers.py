# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummyhead = ListNode(0)
        ptr = dummyhead
        p1 = l1
        p2 = l2
        carry, val = 0, 0
        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            val = val1 + val2 + carry
            carry = 1 if val >= 10 else 0
            val %= 10
            ptr.next = ListNode(val)
            ptr = ptr.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        if carry:
            ptr.next = ListNode(carry)
        return dummyhead.next
