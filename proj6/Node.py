#Odell Dotson and Ethan Prihar, ocdotson@wpi.edu ebprihar@wpi.edu, Intro to AI Project 5

import random

class Node:

	def __init__(self, name, probabiltyList):
		self.name = name
		self.parents = []
		self.probabilty = list(probabiltyList)
		self.truth = -1

	def addParents(self, parentList):
		self.parents = list(reversed(parentList))

	def getTruthLW(self):
		state = ""
		for parent in self.parents:
			state = state + str(parent.getTruth())
		if state == "":
			pos = 0
		else:
			pos = int(state, 2)
		if(random.random() < self.probabilty[pos]):
			truth = 1
		else:
			truth = 0


		return (weight, truth)

	def getTruthRS(self):		
		state = ""
		for parent in self.parents:
			truth = parent.getTruthRS()
			if truth = -1:
				return -1
			state = state + str(truth)
		if state == "":
			pos = 0
		else:
			pos = int(state, 2)
		if(random.random() < self.probabilty[pos]):
			sample = 1
		else:
			sample = 0
		if self.truth == -1
			return sample
		elif sample == self.truth:
			return sample
		else:
			return -1
