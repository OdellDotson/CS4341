#Odell Dotson and Ethan Prihar, ocdotson@wpi.edu ebprihar@wpi.edu, Intro to AI Project 6, Bayes nets
from Node import Node
import sys
import random

nodeList = []
queryNode = -1

def rejectionSampling(samples):
    global queryNode
    global nodeList
    numOfTrue = 0.0
    numTotal = 0.0
    for x in xrange(0, samples):
        sample = nodeList[queryNode].getTruthRS()
        if sample != -1:
            numOfTrue += sample
            numTotal += 1
    if numTotal == 0:
        print "Not enough samples to create a model!"
        return ""
    else:
        return float(numOfTrue) / float(numTotal)


def likelihoodWeighting(samples):
    global queryNode
    global nodeList
    weightOfTrue = 0.0
    weightTotal = 0.0
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
    numOfTrue = 0.0
    numTotal = 0.0
    error = 0.0
    doWhile = True
    currState = 1
    prevState = 0

    while error > .0001 or doWhile or error == 0:
        doWhile = False
        sample = nodeList[queryNode].getTruthRS()
        while sample == -1:
            sample = nodeList[queryNode].getTruthRS()
        if sample != -1:
            numOfTrue += sample
            numTotal += 1

            currState = float(numOfTrue) / float(numTotal)
            error = abs(currState - prevState)
            #print "Error: ", error
            prevState = float(numOfTrue) / float(numTotal)

    print "Runs for rejection sampling: ",  numTotal
    print "Rejection sampling with convergence: ", float(numOfTrue) / float(numTotal)
    return float(numOfTrue) / float(numTotal)


def LWConverge():
    global queryNode
    global nodeList
    weightOfTrue = 0.0
    weightTotal = 0.0
    error = 0.0
    doWhile = True
    currState = 1
    prevState = 0
    runs = 0
    while error > .0001 or doWhile or error == 0:
        doWhile = False
        sample = nodeList[queryNode].getTruthLW()
        if sample[1] == 0:
            weightTotal += sample[0]
        else:
            weightOfTrue += sample[0]
            weightTotal += sample[0]

        currState = float(weightOfTrue) / float(weightTotal)

        error = abs(currState - prevState)

        prevState = currState
        runs += 1

    print "Runs for likelihood weighting: ", runs
    print "Likelihood weighting with convergence:  ", float(weightOfTrue) / float(weightTotal)
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


random.seed()

if int(sys.argv[3]) == -1:
    RSConverge()
    LWConverge()
elif int(sys.argv[3]) == -2:
    for i in xrange (0,5):
        probRej = []
        probLik = []
        for j in xrange(0,10):
            probRej.append(rejectionSampling(i * 200 + 200))
            probLik.append(likelihoodWeighting(i * 200 + 200))
        meanRej = float(sum(probRej)) / float(len(probRej))
        meanLik = float(sum(probLik)) / float(len(probLik))
        diffRej = []
        diffLik = []
        for val in probRej:
            diffRej.append((val - meanRej)*(val - meanRej))
        for val in probLik:
            diffLik.append((val - meanLik)*(val - meanLik))
        varRej = float(sum(diffRej)) / float(len(diffRej))
        varLik = float(sum(diffLik)) / float(len(diffLik))

        print "Rejection sampling of ", i * 200 + 200, " samples:"
        print "mean: ", meanRej
        print "variance: ", varRej
        print "Likelihood weighting of ", i * 200 + 200, " samples:"
        print "mean: ", meanLik
        print "variance: ", varLik
else:
    print "Rejection sampling: " ,rejectionSampling(int(sys.argv[3]))
    print "Likelihood weighting:  ", likelihoodWeighting(int(sys.argv[3]))