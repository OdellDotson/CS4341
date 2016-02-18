global bagList []
global itemList []
global assignedItems[]

def backtracking(items, bags):
	finished = False 												# wheather or not we are done with the search
	backtracking = False 											# wheather or not we are backtracking
	currentItem = 0 												# the current item we are placing in a bag
	currentBag = 0 													# the current bag we are trying to place the item in
	while not finished: 											# as long as we are still searching for a solution
		while not backtracking: 									# if we are not backtracking
			if items[currentItem].canBeIn(bags[currentBag]): 		# if we can place the current item in the current bag
				bags[currentBag].addItem(items[currentItem]) 		# add the item to the bag
				if currentItem == len(items) - 1: 					# if the last item is placed in a bag
					if finalCheck: 									# check if all the criteria are met
						finished = True 							# if they are, then we are finished
					else: 											# if they are not
						backtracking = True 						# start to backtrack
				else: 												# if we have just placed an item that is not the last item in a bag
					currentItem += 1 								# move on to the next item
					currentBag = 0 									# start by trying to place the next item in the first bag
			else if currentBag == len(bags - 1): 					# if the item could not be placed in any of the bags
				backtracking = True 								# start to backtrack
			else: 													# if the item cannot be placed in this bag
				currentBag += 1 									# try to place the item in the next bag
		while backtracking: 										# if we are backtracking
			if currentBag == 0: 									# if this is the first item
				finished = True 									# there is no solution to this problem
			else: 													# if we have not determined that there is no solution
				currentItem -= 1 									# go back to the last item
				for i in xrange(0,len(bags) - 1): 					# for every bag
					if bags[i].equals(Items[currentItem].inBag): 	# if the last item was placed in this bag
						currentBag = i 								# set the current bag to be the bag the last item was placed in
				Items[currentItem].inBag.removeLastItem() 			# take the last item out of the bag it was placed in
				if currentBag != len(bags - 1): 					# if the bag the last item was in was not the last bag it could be placed in
					currentBag += 1 								# move on to the next bag it could be placed in
					backtracking = False 							# stop backtracking
