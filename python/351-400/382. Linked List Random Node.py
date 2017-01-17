class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        n = 0
        node = self.head
        while node:
            n += 1
            node = node.next
        node = self.head
        for _ in xrange(random.randrange(n)):
            node = node.next
        return node.val
