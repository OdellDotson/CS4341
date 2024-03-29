#Odell Dotson and Ethan Prihar, ocdotson@wpi.edu ebprihar@wpi.edu, Intro to AI Project 6, Bayes nets

import random

class Node:

    def __init__(self, name, probabiltyList):
        self.name = name
        self.parents = []
        self.probability = list(probabiltyList)
        self.truth = -1

    def addParents(self, parentList):
        self.parents = list(reversed(parentList))

    def getTruthLW(self):
        state = ""
        weight = 1
        for parent in self.parents:
            temp = parent.getTruthLW()
            state += str(temp[1])
            weight *= temp[0]
        if state == "":
            pos = 0
        else:
            pos = int(state, 2)
        if self.truth == 1:
            truth = 1
            weight *= self.probability[pos]
        elif self.truth == 0:
            truth = 0
            weight *= (1 - self.probability[pos])
        else:
            if random.random() < self.probability[pos]:
                truth = 1
            else:
                truth = 0
        return [weight, truth]

    def getTruthRS(self):
        state = ""
        for parent in self.parents:
            truth = parent.getTruthRS()
            if truth == -1:
                return -1
            state += str(truth)
        if state == "":
            pos = 0
        else:
            pos = int(state, 2)
        if random.random() < self.probability[pos]:
            sample = 1
        else:
            sample = 0
        if self.truth == -1:
            return sample
        elif sample == self.truth:
            return sample
        else:
            return -1
