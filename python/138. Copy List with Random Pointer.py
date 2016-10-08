# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        table = {}
        table[id(None)] = None
        ptr = head
        while ptr:
            table[id(ptr)] = RandomListNode(ptr.label)
            ptr = ptr.next
        ptr = head
        while ptr:
            node = table[id(ptr)]
            node.next = table[id(ptr.next)]
            node.random = table[id(ptr.random)]
            ptr = ptr.next
        return table[id(head)]
        
        
            
            
        