class Bag:
	
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.items = []
		self.totalWeight = 0
		self.percentFull = 0
		self.isFull = False
		self.isFullEnough = False

	def addItem(self, item):
		self.items.append(item)
		item.inBag = self
		item.isInBag = True
		self.totalWeight = totalWeight + item.weight
		self.percentFull = int(capacity / totalWeight)
		if percentFull == 100:
			self.isFull = True
		if percentFull >= 90:
			isFullEnough = True

	def removeItem(self, item):
		self.items.remove(item) # this will throw an error if the item is not in the list, I don't know if the build in function can look for objects or just values
		item.inBag = Bag(noBag, 0)
		item.isInBag = False
		self.totalWeight = totalWeight - item.weight
		self.percentFull = int(capacity / totalWeight)
		if percentFull != 100:
			self.isFull = False
		if percentFull < 90:
			isFullEnough = False

	def equals(self, other):
		if self.name == other.name:
			return True
		else:
			return False