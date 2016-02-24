from Node import Node
import Net
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
    return numOfTrue / numTotal

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


        #print "Name data: ",nameData
        #print "Parent list: ", parList
        #print "Prob list: ", probList, "\n"

        nodeList.append(Node(nameData, probList))
        nodeParents.append(parList)
    #print nodeParents
    for x in range (0, len(nodeList)):
        #print "Child: ", nodeList[x].name, ", parents: "
        parentList = []
        for parentName in nodeParents[x]:
            for nodesThatMayBeParents in nodeList:
                if nodesThatMayBeParents.name == parentName:
                    parentList.append(nodesThatMayBeParents)
        #print parentList
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