from Bag import Bag

class Item:

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.inBag = Bag("noBag", 0)
		self.isInBag = False
		self.allowedBags = [] # list of bags that this item can be in
		self.mustBeWith = [] # list of items that must be in the same bag as this item
		self.cantBeWith = [] # list of items that cannot be in the same bad as this item
		self.partnerItems = [] # Mutually exclusive items. Empty if this item does not have a mutually inclusive binary constraint.
		self.partnerBags = [] # the bags that the mutually exclusive items can be in, all arrays of 2 bags
		self.heuristic = 0

	# This function will return true if an item is allowed in a bag and false if it is not.
	def canBeIn(self, bag):
		if bag not in self.allowedBags: # if this item is forbid from being in the bag
			return False
		for item in self.cantBeWith: # if there is an item in the bag that this item cannot be with
			if item in bag.items:
				return False
		for item in self.mustBeWith: # if there is an item that this item must be with in a different bag
			if item.isInBag and not item.inBag.equals(bag):
				return False
		if bag.totalWeight + self.weight > 100: # if the bag will be over capacity if this item is placed in it
			return False
		if bag.numItems == bag.maxItems:
			return False
		# @TODO
		# read this so that you understand what has been changed
		for i in xrange(0, len(partnerItems) - 1):
			if self.partnerItems[i].inBag in partnerBags[i] and self.partnerItems[i].inBag.equals(bag): # if this item's mutual inclusive partner item is in one of the mutual bags and that bag is the bag
				return False
			if self.partnerItems[i].inBag in self.partnerBags[i] and bag not in self.partnerBags[i]: # if this item's mutual inclusive partner item is in one of the mutual bags and the bag is not a mutual bag
				return False
			if self.partnerItems[i].inBag not in self.partnerBags[i]: # if the partner item is not in a partner bag
				for partnerBag in self.partnerBags[i]:
					if partnerBag.equals(bag):
						return False
		return True

	def makeHeuristic(self): # tries to quantify how constrained the item is, lower value equals more constrained
		self.heuristic = 3 * len(self.allowedBags) - len(self.mustBeWith) - len(self.cantBeWith) - len(self.partnerItems)

	def equals(self, other):
		if self.name == other.name:
			return True
		else:
			return False
