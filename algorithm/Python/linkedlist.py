class Node(object):
	def __init__(self, data, next = None):
		self.data = data
		self.next = next
	def set_data(self, data):
		self.data = data
	def get_data(self):
		return self.data
	def set_next(self, node):
		self.next = node
	def get_next(self):
		return self.next
class Linkedlist(object):
	def __init__(self,head = None):
		self.head = head
		self.count = 0

	def insert_head(self, node):
		node.set_next(self.head)
		self.head = node
		self.count += 1

	def insert_tail(self, node):
		cur = self.head
		node.set_next(None)
		if cur:
			while cur.get_next():
				cur = cur.get_next()
			cur.set_next(node)
		else:
			self.head = node
	def remove(self, data):
		if self.head.get_data() == data:
			self.head = self.head.get_next()
		else:
			cur = self.head
			while cur:
				pre = cur
				cur = cur.get_next()
				if cur.get_data() == data:
					pre.set_next(cur.get_next())
					return

	def search(self, data):
		cur = self.head
		while cur:
			if cur.get_data() == data:
				return cur
			cur = cur
		return None
	def printall(self):
		cur = self.head
		while cur:
			print cur.get_data()
			cur = cur.get_next()


linkedlist = Linkedlist()
for i in range(100):
	node = Node(i)
	linkedlist.insert_tail(node)
linkedlist.printall()
linkedlist.remove(99)
linkedlist.printall()
