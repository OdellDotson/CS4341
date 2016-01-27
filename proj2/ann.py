# This is the project.
# Odell "Vorpal Bunny" Dotson && Ethan "The Floorboards of Heaven" Prihar

import sys
import numpy
import random

data = []
inputArray = numpy.array([])
outputArray = numpy.array([])
inputArrayFull = numpy.array([])
outputArrayFull = numpy.array([])
numHiddenNodes = 0
holdOutPercent = 0

outputGuess = numpy.array([])
inputToHiddenWeight =  numpy.array([])
hiddenToOutputWeight =  numpy.array([])

# #################################################################################################################### #
# ###################################################_FUNCTIONS_###################################################### #
# #################################################################################################################### #

def getData(fileName):
    """This function retrieves all the data from the specified text document.

    This function retrieves all the data from the specified text document and stores it in the global arrays.

    :param fileName: The name of the the file to get data from.
    """
    dataFile = open(fileName, 'r')
    dataPointsTotal = 0
    for line in dataFile:
        dataPointsTotal += 1
    dataFile.close()
    dataFile = open(fileName, 'r')

    global inputArray
    global inputArrayFull
    global outputArray
    global outputArrayFull

    numberOfLine = 0
    for line in dataFile: # For each line in the data file
        lineInfo = line.split(" ")
        sanitizedLineInfo = []
        for elt in lineInfo:
            sanitizedLineInfo.append(float(elt))
        numpy.append(inputArrayFull,([sanitizedLineInfo[0],sanitizedLineInfo[1]]))
        numpy.append(outputArrayFull,(sanitizedLineInfo[2]))
        data.append(sanitizedLineInfo)
        numberOfLine += 1
    dataFile.close()

    print inputArrayFull

    learningPortion = ((100-holdOutPercent)/100)

    for x in xrange(0, int( (len(data) * learningPortion )) -1):
        print x
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

    random.seed([420]) #None so that we use current system time.

    inputSize = len(data[0]) -1

    global inputToHiddenWeight
    global hiddenToOutputWeight

    inputToHiddenWeight = 2*numpy.random.random((int(inputSize),int(numHiddenNodes))) - 1
    hiddenToOutputWeight = 2*numpy.random.random((int(numHiddenNodes),1)) - 1


def sig(x):
    """ Gets the value of the sigmoid at x.

    :param x: Where we get the sigmoid value at.
    :return: The sigmoid value at x.
    """
    return 1.0/(1.0+numpy.exp(-x))


def sigD(x):
    """ Gets the derivative of a sigmoid at point x.

    :param x: The point at which we evaluate the derivative of the sigmoid.
    :return: The value of the definite of the sigmoid at x.
    """
    return x*(1.0-x)

def backProp():
    global inputToHiddenWeight
    global hiddenToOutputWeight
    global outputGuess

    # propagate through the neural network by feeding forward
    sigV = numpy.vectorize(sig)
    sigDV = numpy.vectorize(sigD)

    hiddenValues = sig(numpy.dot(inputArray,inputToHiddenWeight))
    outputGuess = sig(numpy.dot(hiddenValues,hiddenToOutputWeight))
    #print outputGuess
    for i in xrange (0,len(outputGuess)):
        if outputGuess[i] < .5:
            outputGuess[i] = 0
        else:
            outputGuess[i] = 1
    # Calculating error:
    outputMisses = outputArray - outputGuess
    #print outputMisses
    # This provides a weighted error
    outputError = outputMisses * sigD(outputGuess)
    #print outputError

    hiddenContribution = numpy.dot(outputError,hiddenToOutputWeight.T)
    # This provides a weighted error
    hiddenError = hiddenContribution * sigD(hiddenValues)

    # Update the weights:
    inputToHiddenWeight += numpy.dot(inputArray.T,hiddenError)
    hiddenToOutputWeight += numpy.dot(hiddenValues.T,outputError)

    """print "Output guess, then input to hidden, then hidden to output."
    print outputGuess
    print inputToHidden
    print hiddenToOutput"""


def calcErrorPercent():
    total = outputArray.size()
    error = 0.0
    for i in range (0, total):
        if outputArray[i] != outputGuess[i]:
            error += 1
    return error / total * 100.0

def holdoutTest():
    global inputArray
    global outputArray
    global inputArrayHeld
    global outputArrayHeld
    inputArray = inputArrayHeld
    outputArray = outputArrayHeld
    backProp()
    print "The error is: " + calcErrorPercent()



# #################################################################################################################### #
# #####################################################_MAIN_######################################################### #
# #################################################################################################################### #

# Read all the data and place it in arrays
setup()
# Run backpropigation untill the error % is below the threshold
backProp()
while(calcErrorPercent > 10):
    backProp()
# Test the nerual network on the holdout data
holdoutTest()
