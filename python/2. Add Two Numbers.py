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
        carry = 0
        while p1 and p2:
            val = p1.val + p2.val + carry
            if val >= 10:
                val = val % 10
                carry = 1
            else:
                carry = 0
            ptr.next = ListNode(val)
            ptr = ptr.next
            p1 = p1.next
            p2 = p2.next
        while p1:
            val = p1.val + carry
            if val >= 10:
                val = val % 10
                carry = 1
            else:
                carry = 0
            ptr.next = ListNode(val)
            ptr = ptr.next
            p1 = p1.next
        while p2:
            val = p2.val + carry
            if val >= 10:
                val = val % 10
                carry = 1
            else:
                carry = 0
            ptr.next = ListNode(val)
            ptr = ptr.next
            p2 = p2.next
        if carry:
            ptr.next = ListNode(carry)
        return dummyhead.next
