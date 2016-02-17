class Item:

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.inBag = Bag(noBag, 0)
		self.isInBag = False
		allowedBags = [] # list of bags that this item can be in
		mustBeWith = [] # list of items that must be in the same bag as this item
		cantBeWith = [] # list of items that cannot be in the same bad as this item

	def canBeIn(self, bag):
		if bag not in allowedBags:
			return False
		for item in cantBeWith:
			if item in bag.items:
				return False
		for item in mustBeWith:
			if item.isInBag and not item.inBag.equals(bag):
				return False
		if bag.totalWeight + self.weight > 100:
			return False
		return True

	def equals(self, other):
		if self.name == other.name:
			return True
		else:
			return False