# This is the project.
# Odell "Vorpal Bunny" Dotson && Ethan "The Floorboards of Heaven" Prihar

import sys
import numpy
import random

data = []
inputArray = numpy.array([])
outputArray = numpy.array([])
inputArrayHeld = numpy.array([])
outputArrayHeld = numpy.array([])
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
    global inputArrayHeld
    global outputArrayHeld

    numberOfLine = 0
    for line in dataFile: # For each line in the data file
        lineInfo = line.split(" ")
        sanitizedLineInfo = []
        for elt in lineInfo:
            sanitizedLineInfo.append(float(elt))
        xypair = [sanitizedLineInfo[0],sanitizedLineInfo[1]]
        inputArrayFull = numpy.append(inputArrayFull,xypair, axis = numberOfLine)
        print outputArrayFull
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        outputArrayFull = numpy.append(outputArrayFull,(sanitizedLineInfo[2]), axis = numberOfLine)

        data.append(sanitizedLineInfo)
        numberOfLine += 1
    dataFile.close()

    print "Fulls"
    print inputArrayFull
    print outputArrayFull

    learningPortion = ((100-holdOutPercent)/100)

    for x in xrange(0, len(outputArrayFull)):
        if(x < int(len(outputArrayFull)*learningPortion)):
            inputArray = numpy.append(inputArray,[(inputArrayFull[x])])
            outputArray = numpy.append(outputArray,(outputArrayFull[x]))
        else:
            inputArrayHeld = numpy.append(inputArray,(inputArrayFull[x]))
            outputArrayHeld = numpy.append(outputArray,(outputArrayFull[x]))

    print "Data given:"
    print inputArray
    print outputArray
    print "Data Withheld:"
    print inputArrayHeld
    print outputArrayHeld


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

    random.seed(420) #None so that we use current system time.

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
    """for i in xrange (0,len(outputGuess)):
        if outputGuess[i] < .5:
            outputGuess[i] = 0
        else:
            outputGuess[i] = 1"""
    # Calculating error:
    outputMisses = outputArray - outputGuess
    #print outputMisses
    # This provides a weighted error
    outputError = outputMisses * sigD(outputGuess)
    #print outputError

    hiddenContribution = outputError.dot(hiddenToOutputWeight.T)
    # This provides a weighted error
    hiddenError = hiddenContribution * sigD(hiddenValues)

    # Update the weights:
    inputToHiddenWeight += inputArray.T.dot(hiddenError)
    hiddenToOutputWeight += hiddenValues.T.dot(outputError)

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


# #################################################################################################################### #
# #####################################################_MAIN_######################################################### #
# #################################################################################################################### #

setup()

numHiddenNodes = sys.argv[2]
holdOutPercent = sys.argv[3]

random.seed(420) #None so that we use current system time.

inputSize = 2

global inputToHiddenWeight
global hiddenToOutputWeight

inputToHiddenWeight = 2*numpy.random.random((3,int(numHiddenNodes))) - 1
hiddenToOutputWeight = 2*numpy.random.random((int(numHiddenNodes),1)) - 1

print inputToHiddenWeight
print hiddenToOutputWeight

backProp()
j=0
while(j < 100000):
    backProp()
    if(j%10000 == 0):
        print "Guesses:"
        global outputGuess
        print outputGuess
        print j
    j+=1
