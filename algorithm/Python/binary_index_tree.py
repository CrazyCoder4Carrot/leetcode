class FenwickTree(object):
	"""docstring for FenwickTree"""
	def __init__(self, n):
		self.sum_arr = [0] * (n + 1)
		self.n = n
	def lowbit(self, x):
		return x & -x
	def update(self, x, val):
		x = x + 1
		while x <= self.n:
			self.sum_arr[x] += val
			x += self.lowbit(x)
	def sum(self,x):
		res = 0
		x += 1
		while x > 0:
			res += self.sum_arr[x]
			x -= self.lowbit(x)
		return res
	def construct(self, arr):
		for i in range(self.n):
			self.update(i, arr[i])
a = [1,2,3,4,5,6]
fen = FenwickTree(len(a))
fen.construct(a)
print fen.sum_arr