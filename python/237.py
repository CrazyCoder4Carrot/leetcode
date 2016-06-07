class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
	def __init__(self,head = None):
		self.head = head
		self.count = 0

	def insert_head(self, node):
		node.next = self.head
		self.head = node
		self.count += 1

	def insert_tail(self, node):
		cur = self.head
		node.next = None
		if cur:
			while cur.next:
				cur = cur.next
			cur.next = node
		else:
			self.head = node
	def deleteNode(self, node):
		data = node.val
		if self.head is None:
			return 
		if self.head.val == data:
			self.head = self.head.next
			return 
		else:
			cur = self.head
			while cur:
				pre = cur
				cur = cur.next
				if cur.val == data:
					pre.next = cur.next
					return
	# def deleteNode(self, ):
	# 	if self.head is None:
	# 		return 
	# 	headval = self.head.get_data()
	# 	nodeval 
	# 	if headval == node.get_data():
	# 		self.head = self.head.get_next()
	# 	else:
	# 		cur = self.head
	# 		while cur:
	# 			pre = cur
	# 			cur = cur.get_next()
	# 			curval = cur.get_data()
	# 			nodeval = node.get_data()
	# 			if curval == nodeval:
	# 				pre.set_next(cur.get_next())
	# 				return
	def search(self, data):
		cur = self.head
		while cur:
			if cur.val == data:
				return cur
			cur = cur
		return None
	def printall(self):
		cur = self.head
		while cur:
			print cur.val
			cur = cur.next


linkedlist = Solution()
for i in range(2):
	node = ListNode(i)
	linkedlist.insert_tail(node)
linkedlist.printall()
node = ListNode(0)
linkedlist.deleteNode(node)
linkedlist.printall()
