# This is the project.
# Odell "Write something, Ethan" Dotson && Ethan "The Floorboards of Heaven" Prihar

import sys

data = {}
numHiddenNodes = 0
holdOutPercent = 0

########################################################################################################################
#####################################################_FUNCTIONS_########################################################
########################################################################################################################

def getData(fileName):
    """This function retrieves all the data from the specified text document.

    This function retrieves all the data from the specified text document and stores it in the global dictionary data.

    :param fileName: The name of the the file to get data from.
    """
    dataFile = open(fileName, 'r')
    numberOfLine = 0
    for line in dataFile:
        lineInfo = line.split(" ")
        sanitizedLineInfo = []
        for elt in lineInfo:
            sanitizedLineInfo.append(float(elt))
        data[numberOfLine] = sanitizedLineInfo
        numberOfLine+=1
    dataFile.close()



def setup():
    """Sets up the system and retrieves data.

    This function calls getData to retrieve data and store it globally, as well as read in the
    number of hidden nodes and the percent of hold out that is specified by the user.
    """
    getData(sys.argv[1])
    global numHiddenNodes
    global holdOutPercent
    numHiddenNodes = sys.argv[2]
    holdOutPercent = sys.argv[3]


def getPt(arrayToGetFrom, point):
    """ Returns the data at <point> from array <arrayToGetFrom> in data.
    This function exists so we can use commands like:
        data.getPt(0,1)
    instead of using the somewhat syntactically complex command:
        (data[0])[1]

    Note that this function is just a wrapper.
    """
    return (data[arrayToGetFrom])[point]

########################################################################################################################
#######################################################_MAIN_###########################################################
########################################################################################################################

setup()
