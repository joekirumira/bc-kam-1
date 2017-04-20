class BinarySearch(list):
	"""docstring for BinarySearch"""

	length = 0
	count = 0
	def __init__(self, listlength, liststeps):
		super(BinarySearch, self).__init__()
		for i in range(liststeps, (liststeps*listlength)+1, liststeps):
			self.append(i)
		self.length = len(self)

	def search(self, target):
		self.count += 1
		min = 0
		max = len(self)-1
		avg = (min+max)/2
		while (min < max):
			if (self[avg] == target):
				return {'count' : self.count, 'index' : avg}
			elif (self[avg] < target):
				self = self[avg+1:]
				return {'count' : self.count, 'index' : avg + 1 + self.search(target)}
			else:
				self = self[:avg]
				return {'count' : self.count, 'index' : self.search(target)}
		return {'count' : self.count, 'index' : avg}
		