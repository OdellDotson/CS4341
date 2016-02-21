#from Item import Item

class Bag:

	def __init__(self, name, capacity, minItems, maxItems):
		self.name = name
		self.capacity = capacity
		self.items = []
		self.totalWeight = 0
		self.percentFull = 0
		self.isFull = False
		self.isFullEnough = False
		self.numItems = 0
		self.minItems = minItems
		self.maxItems = maxItems
		self.heuristic = 0

	# Adds a given item 
	def addItem(self, item):
		self.items.append(item)
		item.inBag = self
		item.isInBag = True
		self.totalWeight = int(self.totalWeight) + int(item.weight)
		self.percentFull = 100*int(int(self.capacity) / self.totalWeight)
		#print self.percentFull
		if self.percentFull == 100:
			self.isFull = True
			self.isFullEnough = True
		if self.percentFull >= 90:
			self.isFullEnough = True

	def removeLastItem(self):
		print self.items[len(self.items)-1].name, " <- ", self.name
		self.items[len(self.items) - 1].inBag = None # Bag("noBag", 0)
		self.items[len(self.items) - 1].isInBag = False
		self.totalWeight = int(self.totalWeight) - int(self.items[len(self.items) - 1].weight)
		self.percentFull = int(self.totalWeight) / int(self.capacity)  # @TODO: This was the other way around, was it supposed to be??
		if self.percentFull != 100:
			self.isFull = False
		if self.percentFull < 90:
			self.isFullEnough = False
		self.items.pop() # this will remove and return the last item in the items list

	def makeHeuristic(self): # tries to quantify how constrained the bag is, lower value equals less constrained
		self.heuristic = -2 * self.capacity - (self.maxItems - self.minItems)

	def equals(self, other):
		if self.name == other.name:
			return True
		else:
			return False