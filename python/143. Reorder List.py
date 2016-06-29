import sys
class Solution(object):
    def reverse(self, head):    
        if not head or not head.next:
            return head
        pre = None
        cur = head
        next = cur.next
        while cur:
            cur.next = pre
            pre = cur
            cur = next
            if next:
                next = next.next
        return pre
    def visit(self, head):
        cur = head
        while cur:
            print cur.val ,
            cur = cur.next
    def findmid(self, head):
        mid = head
        end = head
        while mid and end and end.next:
            mid = mid.next
            end = end.next.next
        return mid
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        cur = head
        mid = self.findmid(head)
        while cur.next != mid:
            cur = cur.next
        cur.next = None
        head2 = self.reverse(mid)
        cur1 = head
        cur2 = head2
        self.visit(head)
        while cur1.next and cur2:
            temp = cur1.next
            cur1.next = cur2
            cur2 = cur2.next
            cur1 = cur1.next
            cur1.next = temp
            cur1 = cur1.next
        if cur2:
            cur1.next = cur2
        return