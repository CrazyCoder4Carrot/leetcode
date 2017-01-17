class Backtrcking():
	def __init__(self, length):
		self.length = length
		self.res = []
	def combine(self, candidiates, depth, path):
		if depth == self.length:
			self.res.append(path)
			return
		for i in range(len(candidiates)):
			self.combine(candidiates, depth + 1, path+[candidiates[i]])
bc = Backtrcking(4)
list = [1,2,3,4]
bc.combine(list, 0, [])
print bc.res



