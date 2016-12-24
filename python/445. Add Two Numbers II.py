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
        stack1 = []
        stack2 = []
        ptr1, ptr2 = l1, l2
        head = ListNode(0)
        ptr = head
        while ptr1:
            stack1.append(ptr1.val)
            ptr1 = ptr1.next
        while ptr2:
            stack2.append(ptr2.val)
            ptr2 = ptr2.next
        carry = 0
        num = 0
        while stack1 and stack2:
            num = stack1.pop() + stack2.pop() + carry
            if num >= 10:
                num = num%10
                carry = 1
            else:
                carry = 0
            temp = ListNode(num)
            temp.next = ptr.next
            ptr.next = temp
        while stack1:
            num = stack1.pop() + carry
            if num >= 10:
                num = num % 10
                carry = 1
            else:
                carry = 0
            temp = ListNode(num)
            temp.next = ptr.next
            ptr.next = temp
        while stack2:
            num = stack2.pop() + carry
            if num >= 10:
                num = num % 10
                carry = 1
            else:
                carry = 0
            temp = ListNode(num)
            temp.next = ptr.next
            ptr.next = temp
        if carry:
            temp = ListNode(carry)
            temp.next = ptr.next
            ptr.next = temp
        return head.next