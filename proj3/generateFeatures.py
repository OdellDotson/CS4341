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

def bottomLeftCornerControl():
    """
    Which player has control over the bottom left corner. ??
    """

def moreInCenerOfBoard():
    """
    Which player has more in the collumns that are not in the left or right extremes.
    """

def centerControl():
    """center disc: discs in the center column owned by each player
    centerControl is the difference of the number of center discs between the first player and the second player.
    Type: Numeric"""
    pass

def openRun():
    """Open discs : Pairs or triplets of connected discs that a player can still build off of. These sets of discs can be horizontal, vertical, or diagonal.
    OpenRun: the difference of the number of open discs between the first player and the second player.
    Type: Numeric"""


def openFirstLevel():
    """Open bottom discs: the number of open discs on the bottom row in the connect-4 board.
    OpenFirstLevel: the number of open bottom discs
    Type:Numeric"""


def moreInCenter():
    """center disc: discs not located in the outermost columns (The first and last column)
    MoreInCenter: the player who has more center discs, otherwise 0 which indicates a tie.
    Type: Nominal"""


def scoreOccupied():
    """
    ScoreBoard: The number of possible connect-4 paths still available to each player.
    ScoreOccupied: the difference between scoreBoard of the first player and  the second player.
    Type: Numeric
    """


def firstRun():
    """
    The player who makes the next move after given board.
    Type: Nominal
    """


