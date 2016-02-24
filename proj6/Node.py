#Odell Dotson and Ethan Prihar, ocdotson@wpi.edu ebprihar@wpi.edu, Intro to AI Project 5

import random

class Node:

	def __init__(self, name, probabiltyList):
		self.name = name
		self.parents = []
		self.probabilty = list(truthList)
		self.truth = -1

	def addParents(parentList):
		self.parents = list(reversed(parentList))

	def getTruth(self):
		state = ""
		for parent in self.parents:
			state = state + str(parent.getTruth())
		if (self.truth == -1):
			pos = int(state, 2)
			if(random.random() < probabilty[pos]):
				return 1
			else:
				return 0
		else:
			return self.truth