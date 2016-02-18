import Item.py

class Bag:
	
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.items = []
		self.totalWeight = 0
		self.percentFull = 0
		self.isFull = False
		self.isFullEnough = False

	# Adds a given item 
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

	def removeLastItem(self):
		self.items[len(self.items) - 1].inBag = Bag(noBag, 0)
		self.items[len(self.items) - 1].isInBag = False
		self.totalWeight = self.totalWeight - self.items[len(self.items) - 1].weight
		self.percentFull = int(self.capacity / self.totalWeight)
		if percentFull != 100:
			self.isFull = False
		if percentFull < 90:
			isFullEnough = False
		self.items.pop() # this will remove and return the last item in the items list

	def equals(self, other):
		if self.name == other.name:
			return True
		else:
			return False