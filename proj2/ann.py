# This is the project.
# Odell "Write something, Ethan" Dotson && Ethan "The Floorboards of Heaven" Prihar

import sys
import numpy
import random

data = []
inputArray = numpy.array([])
outputArray =  numpy.array([])
inputArrayFull =  numpy.array([])
outputArrayFull =  numpy.array([])
numHiddenNodes = 0
holdOutPercent = 0
inputToHidden =  numpy.array([])
hiddenToOutput =  numpy.array([])

# #################################################################################################################### #
# ###################################################_FUNCTIONS_###################################################### #
# #################################################################################################################### #

def getData(fileName):
    """This function retrieves all the data from the specified text document.

    This function retrieves all the data from the specified text document and stores it in the global arrays.

    :param fileName: The name of the the file to get data from.
    """
    dataFile = open(fileName, 'r')
    numberOfLine = 0
    for line in dataFile: # For each line in the data file
        lineInfo = line.split(" ")
        sanitizedLineInfo = []
        for elt in lineInfo:
            sanitizedLineInfo.append(float(elt))
        numpy.append(inputArrayFull,[sanitizedLineInfo[0],sanitizedLineInfo[1]])
        numpy.append(outputArrayFull,(sanitizedLineInfo[2]))
        data.append(sanitizedLineInfo)
        numberOfLine+=1
    dataFile.close()

    learningPortion = ((100-holdOutPercent)/100)

    for x in xrange(0, int( (len(data) * learningPortion ))):
        numpy.append(inputArray,(inputArrayFull[x]))
        numpy.append(outputArray,(outputArrayFull[x]))


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

    random.seed() #None so that we use current system time.

    inputSize = len(data[0]) -1

    global inputToHidden
    global hiddenToOutput

    inputToHidden = 2*numpy.random.random((int(inputSize),int(numHiddenNodes))) - 1
    hiddenToOutput = 2*numpy.random.random((int(numHiddenNodes),1)) - 1


def sig(x):
    """ Gets the value of the sigmoid at x.

    :param x: Where we get the sigmoid value at.
    :return: The sigmoid value at x.
    """
    return 1/(1+numpy.exp(-x))


def sigD(x):
    """ Gets the derivative of a sigmoid at point x.

    :param x: The point at which we evaluate the derivative of the sigmoid.
    :return: The value of the definite of the sigmoid at x.
    """
    return x*(1-x)

########################################################################################################################
#######################################################_MAIN_###########################################################
########################################################################################################################

setup()
# propigate through the neural network by feeding foreward
hiddenValues = sig(numpy.dot(inputArray,inputToHidden))
outputGuess = sig(numpy.dot(hiddenValues,hiddenToOutput))

# Calculating error:
outputMisses = outputArray - outputGuess
outputError = outputMisses * sigD(outputGuess)

hiddenContribution = numpy.dot(outputError,hiddenToOutput.T)
hiddenError = hiddenContribution * sigD(hiddenValues)

# Update the weights:
inputToHidden = numpy.dot(inputArray.T,hiddenError)
hiddenToOutput = numpy.dot(hiddenValues.T,outputError)
