from Bag import Bag
from Item import Item
from Tools import removeNonAscii

itemList = []
bagList = []
fittingLimits = [0,0]

def sortObjects(): # this will sort the items and bags by how constrained they are
	global itemList
	global bagList
	for item in ItemList:
		item.makeHeuristic()
	for bag in bagList:
		bag.makeHeuristic()
	itemList.sort(key = lambda x: x.heuristic) # this might not work, it is from google
	bagList.sort(key = lambda x: x.heuristic) # this might not work, it is from google

def backtracking():
	global bagList
	global itemList
    finished = False 													# whether or not we are done with the search
    backtracking = False 												# whether or not we are backtracking
    currentItem = 0 													# the current item we are placing in a bag
    currentBag = 0 														# the current bag we are trying to place the item in
    while not finished: 												# as long as we are still searching for a solution
        while not backtracking: 										# if we are not backtracking
            if itemList[currentItem].canBeIn(bagList[currentBag]): 		# if we can place the current item in the current bag
                bagList[currentBag].addItem(itemList[currentItem]) 		# add the item to the bag
                if currentItem == len(itemList) - 1: 					# if the last item is placed in a bag
                    if finalCheck: 										# check if all the criteria are met
                        finished = True 								# if they are, then we are finished
                    else: 												# if they are not
                        backtracking = True 							# start to backtrack
                else: 													# if we have just placed an item that is not the last item in a bag
                    currentItem += 1 									# move on to the next item
                    currentBag = 0 										# start by trying to place the next item in the first bag
            elif currentBag == (len(bagList) - 1): 						# if the item could not be placed in any of the bags
                backtracking = True 									# start to backtrack
            else: 														# if the item cannot be placed in this bag
                currentBag += 1 										# try to place the item in the next bag
        while backtracking: 											# if we are backtracking
            if currentItem == 0: 										# if this is the first item
                finished = True 										# there is no solution to this problem
            else: 														# if we have not determined that there is no solution
                currentItem -= 1 										# go back to the last item
                for i in xrange(0,len(bagList) - 1): 					# for every bag
                    if bagList[i].equals(ItemList[currentItem].inBag): 	# if the last item was placed in this bag
                        currentBag = i 									# set the current bag to be the bag the last item was placed in
                ItemList[currentItem].inBag.removeLastItem() 			# take the last item out of the bag it was placed in
                if currentBag != len(bagList) - 1: 						# if the bag the last item was in was not the last bag it could be placed in
                    currentBag += 1 									# move on to the next bag it could be placed in
                    backtracking = False 								# stop backtracking


def readFile():
    dataFile = open('data/input24.txt', 'r')
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
            print "State change to: ", state
        else:
            if state == 0:
                lineData = line.split(" ")
                itemList.append(Item(lineData[0], lineData[1]))
            elif state == 1:
                lineData = line.split(" ")
                bagList.append(Bag(lineData[0], lineData[1]))
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
                    if itemsToCheck.name == cleanedLineData[0]:
                        for itemPartnerToCheck in itemList:
                            if itemPartnerToCheck.name == cleanedLineData[1]:
                                itemsToCheck.mustBeWith.append(itemPartnerToCheck)
                                itemPartnerToCheck.mustBeWith.append(itemsToCheck)



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
                                itemsToCheck.partnerItem.append(itemPartnerToCheck)
                                itemPartnerToCheck.partnerItem.append(itemsToCheck)
                                for bagsNames in bagList:
                                    if bagsNames.name == cleanedLineData[2]:
                                        itemsToCheck.partnerBags.append(bagsNames)
                                        itemPartnerToCheck.partnerBags.append(bagsNames)
                                    if bagsNames.name == cleanedLineData[3]:
                                        itemsToCheck.partnerBags.append(bagsNames)
                                        itemPartnerToCheck.partnerBags.append(bagsNames)

    # Finish up lists of acceptable bags
    for itemsToCheckBagsAllowed in itemList:
        if len(itemsToCheckBagsAllowed.allowedBags) == 0:
            for allBags in bagList:
                itemsToCheckBagsAllowed.allowedBags.append(allBags)
        print "Bags that ", itemsToCheckBagsAllowed.name, " is allowed in:"
        for bagsAllowed in itemsToCheckBagsAllowed.allowedBags:
            print bagsAllowed.name
        print "Bags that ", itemsToCheckBagsAllowed.name, " must be in a bag with:"
        for bagFriends in itemsToCheckBagsAllowed.mustBeWith:
            print bagFriends.name
        print "Bags that ", itemsToCheckBagsAllowed.name, " must NOT be in a bag with:"
        for bagEnemies in itemsToCheckBagsAllowed.cantBeWith:
            print bagEnemies.name
        for partners in itemsToCheckBagsAllowed.partnerItem:
            print itemsToCheckBagsAllowed.name " is partner of ", itemsToCheckBagsAllowed.name, ":"
            print itemsToCheckBagsAllowed.partnerItem[0].name
            print "Bags it uses mutual inclusive binary constraints with it's partner with:", itemsToCheckBagsAllowed.name, ":"
            for partnerBags in itemsToCheckBagsAllowed.partnerBags:
                print partnerBags.name



readFile()