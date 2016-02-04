# uses the bottom left space as the feature, this is the first required feature
def getFeature1(board):
	return board[0]

# uses which player has more non edge pieces as the feature, this is the second required feature
def getFeature2(board):
	count = 0
	for x in xrange(6,36):
		if board[x] == 1:
			count ++
		else if board[x] == 2:
			count --
	if count > 0:
		return 1
	else if count < 0:
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
			else if x <= 11 or x >= 30:
				count = count + 4 * (1.5 - board[x])
			else if x <= 17 or x >= 24:
				count = count + 8 * (1.5 - board[x])
			else:
				count = count + 16 * (1.5 - board[x])
	if count > 0:
		return 1
	else if count < 0:
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
			else if x <= 11 or x >= 30:
				count = count + 4 * (1.5 - board[x])
			else if x <= 17 or x >= 24:
				count = count + 8 * (1.5 - board[x])
			else:
				count = count + 16 * (1.5 - board[x])
	return count