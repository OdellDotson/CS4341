global bagList []
global itemList []
global assignedItems[]

def backtracking(items, bags):
	finished = False
	backtracking = False
	currentItem = 0
	currentBag = 0
	while not finished:
		while not backtracking:
			if items[currentItem].canBeIn(bags[currentBag]):
				bags[currentBag].addItem(items[currentItem])
				if currentItem == len(items) - 1:
					if finalCheck:
						finished = True
					else:
						backtracking = True
				else:
					currentItem += 1
					currentBag = 0
			else if currentBag == len(bags - 1):
				backtracking = True
			else:
				currentBag += 1
		while backtracking:
