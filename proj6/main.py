#Odell Dotson and Ethan Prihar, ocdotson@wpi.edu ebprihar@wpi.edu, Intro to AI Project 6, Bayes nets
from Node import Node
import sys

nodeList = []
queryNode = -1

def rejectionSampling(samples):
    global queryNode
    global nodeList
    numOfTrue = 0
    numTotal = 0
    for x in xrange(0, samples):
        sample = nodeList[queryNode].getTruthRS()
        if sample != -1:
            numOfTrue += sample
            numTotal += 1
    return float(numOfTrue) / float(numTotal)


def likelihoodWeighting(samples):
    global queryNode
    global nodeList
    weightOfTrue = 0
    weightTotal = 0
    for x in xrange(0, samples):
        sample = nodeList[queryNode].getTruthLW()
        if sample[1] == 0:
            weightTotal += sample[0]
        else:
            weightOfTrue += sample[0]
            weightTotal += sample[0]
    return float(weightOfTrue) / float(weightTotal)

def RSConverge():
    global queryNode
    global nodeList
    numOfTrue = 0
    numTotal = 0
    error = 0
    doWhile = True
    while error > .01 or doWhile:
        doWhile = False
        sample = nodeList[queryNode].getTruthRS()
        if sample != -1:
            numOfTrue += sample
            numTotal += 1
            error = abs(error - float(numOfTrue) / float(numTotal))
    return float(numOfTrue) / float(numTotal)


def LWConverge():
    global queryNode
    global nodeList
    weightOfTrue = 0
    weightTotal = 0
    error = 0
    doWhile = True
    while error > .01 or doWhile:
        doWhile = False
        sample = nodeList[queryNode].getTruthLW()
        if sample[1] == 0:
            weightTotal += sample[0]
        else:
            weightOfTrue += sample[0]
            weightTotal += sample[0]
        error = abs(error - float(weightOfTrue) / float(weightTotal))
    return float(weightOfTrue) / float(weightTotal)

def makeNodes(nodeFileName):
    nodeData = open(nodeFileName, 'r')
    nodeParents = []
    for line in nodeData:
        lineData = line.split(":")
        nameData = lineData[0]

        parList = lineData[1].split("] [")[0].split(" [")[1].split(" ")

        probList = lineData[1].split("] [")[1].split("]")[0].split(" ")
        for i in range (0, len(probList)):
            probList[i] = float(probList[i])

        nodeList.append(Node(nameData, probList))
        nodeParents.append(parList)
    for x in range (0, len(nodeList)):
        parentList = []
        for parentName in nodeParents[x]:
            for nodesThatMayBeParents in nodeList:
                if nodesThatMayBeParents.name == parentName:
                    parentList.append(nodesThatMayBeParents)
        nodeList[x].addParents(parentList)

def processQuery(queryFileName):
    global queryNode
    queryFile = open(queryFileName, 'r')
    queryString = ''
    for line in queryFile:
        if queryString == '':
            queryString = line
    queryList = queryString.split(",")
    for x in range (0, len(queryList)):
        if queryList[x] == 't':
            nodeList[x].truth = 1
        elif queryList[x] == 'f':
            nodeList[x].truth = 0
        elif queryList[x] == '?':
            queryNode = x

makeNodes(sys.argv[1])
processQuery(sys.argv[2])

if sys.argv[3] == -1:
    print "Rejection sampling with convergence: " ,RSConverge(int(sys.argv[3]))
    print "Likelihood weighting with convergence:  ", LWConverge(int(sys.argv[3]))
else:
    print "Rejection sampling: " ,rejectionSampling(int(sys.argv[3]))
    print "Likelihood weighting:  ", likelihoodWeighting(int(sys.argv[3]))