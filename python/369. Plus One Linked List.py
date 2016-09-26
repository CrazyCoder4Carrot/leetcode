# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        num = ""
        ptr = head
        while ptr:
            num += str(ptr.val)
            ptr = ptr.next
        res = int(num) + 1
        res = str(res)
        ptr = head
        if len(res) > len(num):
            while ptr.next:
                ptr = ptr.next
            ptr.next = ListNode(0)
        ptr = head
        i = 0
        while ptr:
            ptr.val = int(res[i])
            i  += 1
            ptr = ptr.next
        return head
        