__author__ = 'odell'

import sys

print sys.argv

def classify():
    if len(sys.argv) != 3:
        print "Please give commands of the form: python generateFeatures.py <given data> <file for featured data to go to>"
    inFileName = sys.argv[1]
    outFileName = sys.argv[2]
    inDataFile = open(inFileName, 'r')
    outDataFile = open(outFileName, 'w')

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
    return count


# Checks who has the greater number of top-of-column control pieces.
def getFeature5(): # Dear future employers: I know this code is shit I have a deadline to meet I'm sorry
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
    elif toAdd == 1:
        yellowTops +=1

    toAdd = 0
    x = 6

    while (x<12 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 1:
        yellowTops +=1

    toAdd = 0
    x = 12

    while (x<18 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 1:
        yellowTops +=1

    toAdd = 0
    x = 18

    while (x<24 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 1:
        yellowTops +=1

    toAdd = 0
    x = 24

    while (x<30 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 1:
        yellowTops +=1

    toAdd = 0
    x = 30

    while (x<36 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 1:
        yellowTops +=1

    toAdd = 0
    x = 36

    while (x<42 and toAdd == 0):
        if board[x] == 0 and x != 0:
                toAdd = board[x-1]
        x+=1
    if toAdd == 1:
        redTops += 1
    elif toAdd == 1:
        yellowTops +=1




getFeature5()

