#Odell Dotson (ocdotson@wpi.edu) and Ethan Prihar (ebprihar@wpi.edu)
#CS4341 Intro to AI, Project 3

import sys

def classify():
    if len(sys.argv) != 3:
        print "Please give commands of the form: python generateFeatures.py <given data> <file for featured data to go to>"
    inFileName = sys.argv[1]
    outFileName = sys.argv[2]
    inDataFile = open(inFileName, 'r')
    outDataFile = open(outFileName, 'w')

    lineNumber = 0
    boardList = []
    boardListFeatures = []

    for line in inDataFile:
        if lineNumber == 0:
            lineNumber += 1
        else:
            dataLine = line.split(",")
            cleanDataLine = []
            for elt in dataLine:
                cleanDataLine.append(int(elt))
            boardList.append(cleanDataLine)
            lineNumber += 1

    lineNumber = 0

    for elt in boardList:
        featured = elt
        featured.append(getFeature1(elt))
        featured.append(getFeature2(elt))
        featured.append(getFeature3(elt))
        featured.append(getFeature4(elt))
        featured.append(getFeature5(elt))

        boardListFeatures.append(featured)
        lineNumber += 1

    outDataFile.write("f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,winner,fe1,fe2,fe3,fe4,fe5\n")
    for elt in boardListFeatures:
        buff = ""
        for x in elt:
            buff = buff + str(x) + ","
        buff = buff[:len(buff)-1]
        buff = buff + '\n'

        outDataFile.write(buff)


# uses the bottom left space as the feature, this is the first required feature
def getFeature1(board):
    return board[0]

# uses which player has more non edge pieces as the feature, this is the second required feature
def getFeature2(board):
    count = 0
    for x in xrange(6,36):
        if board[x] == 1:
            count += 1
        elif board[x] == 2:
            count -= 1
    if count > 0:
        return 1
    elif count < 0:
        return 2
    else:
        return 0

# uses a weight based on the pieces distance from the center to calculate each players value and uses the player with the highest value as the feature
def getFeature3(board):
    count = 0
    for x in xrange(0,42):
        if board[x] != 0:
            if x <= 5 or x >= 36:
                count = count + 2 * (1.5 - board[x])
            elif x <= 11 or x >= 30:
                count = count + 4 * (1.5 - board[x])
            elif x <= 17 or x >= 24:
                count = count + 8 * (1.5 - board[x])
            else:
                count = count + 16 * (1.5 - board[x])
    if count > 0:
        return 1
    elif count < 0:
        return 2
    else:
        return 0

# uses a weight based on the pieces distance from the center and whose piece it is to calculate a value for the board state and returns that value
def getFeature4(board):
    count = 0
    for x in xrange(0,42):
        if board[x] != 0:
            if x <= 5 or x >= 36:
                count = count + 2 * (1.5 - board[x])
            elif x <= 11 or x >= 30:
                count = count + 4 * (1.5 - board[x])
            elif x <= 17 or x >= 24:
                count = count + 8 * (1.5 - board[x])
            else:
                count = count + 16 * (1.5 - board[x])
    return int(count)


# Checks who has the greater number of top-of-column control pieces.
def getFeature5(board): # Dear future employers: I know this code is shit I have a deadline to meet I'm sorry
    redTops = 0
    yellowTops = 0
    toAdd = 0
    x = 0

    while (x<6 and toAdd == 0):
        if board[x] == 0 and x != 0:
            toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 2:
        yellowTops +=1

    toAdd = 0
    x = 6

    while (x<12 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 2:
        yellowTops +=1

    toAdd = 0
    x = 12

    while (x<18 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 2:
        yellowTops +=1

    toAdd = 0
    x = 18

    while (x<24 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 2:
        yellowTops +=1

    toAdd = 0
    x = 24

    while (x<30 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 2:
        yellowTops +=1

    toAdd = 0
    x = 30

    while (x<36 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 2:
        yellowTops +=1

    toAdd = 0
    x = 36

    while (x<42 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 2:
        yellowTops +=1

    return redTops - yellowTops



classify()