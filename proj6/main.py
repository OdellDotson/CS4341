from Node import Node
import Net
import sys

nodeList = []
nodeParents = []

def makeNodes():
    nodeFileName = sys.argv[1]
    nodeData = open(nodeFileName, 'r')
    for line in nodeData:
        lineData = line.split(":")
        nameData = lineData[0]

        parList = lineData[1].split("] [")[0].split(" [")[1].split(" ")

        probList = lineData[1].split("] [")[1].split("]")[0].split(" ")
        for i in range (0, len(probList)):
            probList[i] = float(probList[i])


        print "Name data: ",nameData
        print "Parent list: ", parList
        print "Prob list: ", probList, "\n"

        nodeList.append(Node(nameData, probList))
        nodeParents.append(parList)
    print nodeParents
    for x in range (0, len(nodeList)):
        print "Child: ", nodeList[x].name, ", parents: "
        #print nodeParents[x]
        parentList = []
        for parentName in nodeParents[x]:
            for nodesThatMayBeParents in nodeList:
                if nodesThatMayBeParents.name == parentName:
                    parentList.append(nodesThatMayBeParents)
        nodeList[x].addParents(parentList)

def processQuery():
    queryFileName = sys.argv[2]
    queryFile = open(queryFileName, 'r')
    queryString = ''
    for line in queryFile:
        if queryString == '':
            queryString = line
    queryList = queryString.split(",")
    for t in queryList:
        print t
    numberOfQueryNode = -1
    for x in range (0, len(queryList)):
        if queryList[x] == 't':
            nodeList[x].truth = 1
        elif queryList[x] == 'f':
            nodeList[x].truth = 0
        elif queryList[x] == '?':
            numberOfQueryNode = x
    nodeList[numberOfQueryNode].getTruth()

makeNodes()
processQuery()