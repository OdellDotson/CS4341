#Odell Dotson and Ethan Prihar, ocdotson@wpi.edu ebprihar@wpi.edu, Intro to AI Project 5

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
		self.numItems += 1
		self.items.append(item)
		item.inBag = self
		item.isInBag = True
		self.totalWeight = (self.totalWeight) + (item.weight)
		self.percentFull = 100*int((self.totalWeight)/(self.capacity))
		#print self.percentFull
		if self.percentFull == 100:
			self.isFull = True
			#self.isFullEnough = True
		if self.percentFull >= 90:
			self.isFullEnough = True

	def removeLastItem(self):
		#print self.items[len(self.items)-1].name, " <- ", self.name
		self.items[len(self.items) - 1].inBag = Bag("noBag", 0,0,0)
		self.items[len(self.items) - 1].isInBag = False
		self.totalWeight = (self.totalWeight) - (self.items[len(self.items) - 1].weight)
		self.percentFull = 100*int((self.totalWeight)/(self.capacity))
		if self.percentFull != 100:
			self.isFull = False
		if self.percentFull < 90:
			self.isFullEnough = False
		self.items.pop() # this will remove and return the last item in the items list
		self.numItems -= 1

	def makeHeuristic(self): # tries to quantify how constrained the bag is, lower value equals less constrained
		self.heuristic = -2 * self.capacity - (self.maxItems - self.minItems)

	def equals(self, other):
		if self.name == other.name:
			return True
		else:
			return False