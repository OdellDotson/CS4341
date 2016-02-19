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

		# @TODO: This needs a big restructure so it takes into account the fact that a single item can have multiple partners each with exclusive bag pairings.
		self.partnerItem = [] # Mutually exclusive item. Empty if this item does not have a mutually inclusive binary constraint.

		# How it used to look, for your reference:
		#Item("noItem", 0) # mutually exclusive item

		self.partnerBags = [] # the bags that the mutually exclusive item can be in

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
		if self.partnerItem.inBag in self.partnerBags and self.partnerItem.inBag.equals(bag): # if this item's mutual inclusive partner item is in one of the mutual bags and that bag is the bag
			return False
		if self.partnerItem.inBag in self.partnerBags and bag not in self.partnerBags: # if this item's mutual inclusive partner item is in one of the mutual bags and the bag is not a mutual bag
			return False
		if self.partnerItem.inBag not in self.partnerBags:
			for partnerBag in self.partnerBags:
				if partnerBag.equals(bag):
					return False
		return True

	def equals(self, other):
		if self.name == other.name:
			return True
		else:
			return False
