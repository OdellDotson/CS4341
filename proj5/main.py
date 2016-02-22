#Odell Dotson and Ethan Prihar, ocdotson@wpi.edu ebprihar@wpi.edu, Intro to AI Project 5
from Bag import Bag
from Item import Item
from Tools import removeNonAscii
from numpy import floor
import sys

itemList = []
bagList = []
fittingLimits = [0,9999999]

def sortObjects(): # this will sort the items and bags by how constrained they are
    global itemList
    global bagList
    for item in itemList:
        item.makeHeuristic()
    for bag in bagList:
        bag.makeHeuristic()
    itemList.sort(key = lambda x: x.heuristic) # this might not work, it is from google
    bagList.sort(key = lambda x: x.heuristic) # this might not work, it is from google


def finalCheck(): # checks at the end of backtracking search to make sure all of the conditions are met for the bags
    printFinalState()
    for bag in bagList:
        if bag.numItems < bag.minItems:
            return False
        if not bag.isFullEnough:
            return False
    return True

# this function is called in run in backtracking
# this function is used to test wheather asigning
# an item to a bag prevented any of the unassigned items
# from being able to be placed in a bag. It is
# called after an item is added to a bag in backtrack.
def forwardCheck(): # returns true if assiging an item to a bag eliminates the domain of another item
    global itemList
    global bagList
    noDomain = False
    for item in itemList:
        if not item.isInBag:
            noDomain = True
            for bag in bagList:
                if item.canBeIn(bag):
                    noDomain = False
                else:
                    pass
        if noDomain:
            return True
    return False



def backtrack():
    global bagList
    global itemList
    finished = False 													# whether or not we are done with the search
    backtracking = False 												# whether or not we are backtracking
    currentItem = 0 													# the current item we are placing in a bag
    currentBag = 0 														# the current bag we are trying to place the item in
    while not finished: 												# as long as we are still searching for a solution

        #printFinalState()
        if not backtracking: 										    # if we are not backtracking

            #print "Not backtracking: current item:", itemList[currentItem].name, "current bag: ", bagList[currentBag].name
            if itemList[currentItem].canBeIn(bagList[currentBag]): 		# if we can place the current item in the current bag
                bagList[currentBag].addItem(itemList[currentItem]) 		# add the item to the bag
                #print itemList[currentItem].name, " -> ", bagList[currentBag].name
                if currentItem == len(itemList) - 1: 					# if the last item is placed in a bag

                    if getValidation(): 									# check if all the criteria are met
                        finished = True 								# if they are, then we are finished
                    else: 												# if they are not
                        #print "BTS"
                        backtracking = True 							# start to backtrack
                        currentItem += 1
                else: 													# if we have just placed an item that is not the last item in a bag
                    if forwardCheck():									# if we have made it impossible to place an un placed item in a bag
                        backtracking = True 							# start to backtrack
                        currentItem += 1 								# move on to the next item
                    else:												# if we didn't make it impossible to place an un placed item in a bag
                        currentItem += 1 								# move on to the next item
                        currentBag = 0 									# start by trying to place the next item in the first bag
            elif currentBag == len(bagList) - 1: 					# if the item could not be placed in any of the bags
                backtracking = True 									# start to backtrack
            else: 														# if the item cannot be placed in this bag
                currentBag += 1 										# try to place the item in the next bag
        if backtracking: 											    # if we are backtracking
            currentItem -= 1    										# go back to the last item
            #print "At start of backtracking condition: current item:", itemList[currentItem].name, "current bag: ", bagList[currentBag].name, ", backtracking."

            if currentItem == 0 and itemList[0].inBag.equals(bagList[len(bagList)-1]): 										# if this is the first item
                print "Backtracked all the way, no solution."
                finished = True 										# there is no solution to this problem
            else: 														# if we have not determined that there is no solution
                for i in xrange(0,len(bagList)): 					    # for every bag
                    if bagList[i].equals(itemList[currentItem].inBag): 	# if the last item was placed in this bag
                        currentBag = i 									# set the current bag to be the bag the last item was placed in
                #print "In backtracking condition, about to remove something. current item:", itemList[currentItem].name, "current bag: ", bagList[currentBag].name, ", backtracking."
                itemList[currentItem].inBag.removeLastItem() 			# take the last item out of the bag it was placed in
                if currentBag != len(bagList) - 1: 						# if the bag the last item was in was not the last bag it could be placed in
                    currentBag += 1 									# move on to the next bag it could be placed in
                    backtracking = False 								# stop backtracking

def readFile():
    file = sys.argv[1]
    dataFile = open(file, 'r')
    state = -1
    """
    State 0:
        Adding variables
    State 1:
        Adding values
    State 2:
        fitting limits
    State 3:
        unary inclusive
    State 4:
        unary exclusive
    State 5:
        binary equals
    State 6:
        binary not equals
    State 7:
        binary simultaneous
    """

    for line in dataFile:
        if line[0] == '#':
            state += 1
            #print "State change to: ", state
        else:
            if state == 0:
                lineData = line.split(" ")
                itemList.append(Item(lineData[0], int(lineData[1])))
            elif state == 1:
                lineData = line.split(" ")
                bagList.append(Bag(lineData[0], int(lineData[1]), 0, 0))
            elif state == 2:
                lineData = line.split(" ")
                fittingLimits[0], fittingLimits[1] = (int(removeNonAscii(lineData[0])), int(removeNonAscii(lineData[1]))) #Dumb depackaging thing because python yay
            elif state == 3:
                lineData = line.split(" ")
                cleanedLineData = []
                for term in lineData: # Clean each term of non-ascii formatting characters
                    cleanedLineData.append(removeNonAscii(term))
                for item in itemList: # For each item in our item list
                    if item.name == cleanedLineData[0]: # If we've found the item that this line is describing
                        for nameOfBag in cleanedLineData: #For each element in the cleaned line data. Of course first element will never be the case we want. Looking for bag names.
                            for bag in bagList: # for each of our bags
                                if bag.name == nameOfBag: #If any of our bags are of the name of the item we are setting up inclusive unary constraints:
                                    item.allowedBags.append(bag) #Add that bag to the list of acceptable bags.'
                                    #print "List of bags that ", item.name, "is exclusively allowed in so far:"
                                    #for g in item.allowedBags:
                                        #print g.name

            elif state == 4:
                lineData = line.split(" ")
                cleanedLineData = []

                bagsToAdd = []

                for bagInit in bagList:
                    bagsToAdd.append(bagInit)

                for term in lineData: # Clean each term of non-ascii formatting characters
                    cleanedLineData.append(removeNonAscii(term))
                for item in itemList: # For each item in our item list
                    if item.name == cleanedLineData[0]: # If we've found the item that this line is describing
                        for nameOfBag in cleanedLineData: #For each element in the cleaned line data. Of course first element will never be the case we want. Looking for bag names.
                            for bag in bagList: # for each of our bags
                                if bag.name == nameOfBag: #If any of our bags are of the name of the item we are setting up exclusive unary constraints:
                                    if bag in item.allowedBags:
                                        item.allowedBags.remove(bag) #If the bag was listed in unary exclusion AND unary inclusion. Why that would ever happen, IDK, but it happens in one of the given cases. Ugh. Thanks.
                                    bagsToAdd.remove(bag)
                                    #print "Removing ", bag.name , " bag from ", item.name ,"'s pool of possible bags."
                        #print "Bags it's really ok to add for ", item.name
                        for bagsToReallyAdd in bagsToAdd:
                            item.allowedBags.append(bagsToReallyAdd)
                            #print bagsToReallyAdd.name
            elif state == 5: # Binary Equality
                lineData = line.split(" ")

                cleanedLineData = []

                for itemName in lineData:
                    cleanedLineData.append(removeNonAscii(itemName))

                for itemsToCheck in itemList:
                    if itemsToCheck.name in cleanedLineData:
                        for elt in cleanedLineData:
                            for items in itemList:
                                if items.name == elt:
                                    itemsToCheck.mustBeWith.append(items)

            elif state == 6: # Binary Inequality
                lineData = line.split(" ")

                cleanedLineData = []

                for itemName in lineData:
                    cleanedLineData.append(removeNonAscii(itemName))

                for itemsToCheck in itemList:
                    if itemsToCheck.name == cleanedLineData[0]:
                        for itemPartnerToCheck in itemList:
                            if itemPartnerToCheck.name == cleanedLineData[1]:
                                itemsToCheck.cantBeWith.append(itemPartnerToCheck)
                                itemPartnerToCheck.cantBeWith.append(itemsToCheck)
            else: # state == 7:
                lineData = line.split(" ")

                cleanedLineData = []

                for descriptor in lineData:
                    cleanedLineData.append(removeNonAscii(descriptor))

                for itemsToCheck in itemList:
                    if itemsToCheck.name == cleanedLineData[0]:
                        for itemPartnerToCheck in itemList:
                            if itemPartnerToCheck.name == cleanedLineData[1]: # If we have detected partners:
                                itemsToCheck.partnerItems.append(itemPartnerToCheck)
                                itemPartnerToCheck.partnerItems.append(itemsToCheck)
                                bagArray = []
                                for bagsNames in bagList:
                                    if (bagsNames.name == cleanedLineData[2]) or bagsNames.name == cleanedLineData[3]:
                                        bagArray.append(bagsNames)

                                itemsToCheck.partnerBags.append(bagArray)
                                itemPartnerToCheck.partnerBags.append(bagArray)

    verbose = False
    for itemsToCheckBagsAllowed in itemList:
        if len(itemsToCheckBagsAllowed.allowedBags) == 0:
            for allBags in bagList:
                itemsToCheckBagsAllowed.allowedBags.append(allBags)
        if verbose: print "Bags that ", itemsToCheckBagsAllowed.name, " is allowed in:"
        for bagsAllowed in itemsToCheckBagsAllowed.allowedBags:
            if verbose:print bagsAllowed.name
        if verbose:print "Bags that ", itemsToCheckBagsAllowed.name, " must be in a bag with:"
        for bagFriends in itemsToCheckBagsAllowed.mustBeWith:
            if verbose:print bagFriends.name
        if verbose:print "Bags that ", itemsToCheckBagsAllowed.name, " must NOT be in a bag with:"
        for bagEnemies in itemsToCheckBagsAllowed.cantBeWith:
            if verbose:print bagEnemies.name
        for x in range (0, len(itemsToCheckBagsAllowed.partnerItems)):
            if verbose:print itemsToCheckBagsAllowed.name, "'s first binary simultaneous partner is ", itemsToCheckBagsAllowed.partnerItems[x].name,\
                ", and their bags are "
            for partnerBags in itemsToCheckBagsAllowed.partnerBags[x]:
                if verbose:print partnerBags.name

    for bagsToUpdateMinMax in bagList:
        bagsToUpdateMinMax.minItems = fittingLimits[0]
        bagsToUpdateMinMax.maxItems = fittingLimits[1]

    if len(bagList) > 0:
        if verbose: print "Bags can hold between ", bagList[0].minItems, " and ", bagList[0].maxItems, " items, inclusively."
    if verbose: print "Set up complete."





def printState():
    for bag in bagList:
        header = bag.name
        items = 0
        for item in itemList:
            if not (item.inBag.name == "noBag"):
                if item.inBag.name == bag.name:
                    header = header + " " + item.name
                    items += 1
        print header

def printFinalState():
    for bag in bagList:
        header = bag.name
        items = 0
        for item in itemList:
            if not (item.inBag.name == "noBag"):
                if item.inBag.name == bag.name:
                    header = header + " " + item.name
                    items += 1
        print header
        print "number of items: ", items
        print "total weight: " , bag.totalWeight, "/", bag.capacity
        print "wasted capacity: " , bag.capacity - bag.totalWeight, "\n"

def getValidation():
    for bag in bagList:
        header = bag.name
        items = 0
        for item in itemList:
            if not (item.inBag.name == "noBag"):
                if item.inBag.name == bag.name:
                    header = header + " " + item.name
                    items += 1
        limit  = floor((0.9 * float(bag.capacity)))/float(bag.capacity)
        #print limit
        if items < fittingLimits[0]:
            return False

        elif (float(bag.totalWeight) / float(bag.capacity)) < limit:
            return False
    return True

#print "START"

readFile()
sortObjects()
backtrack()
#print "\n\n\n"
printFinalState()