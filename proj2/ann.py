# This is the project.
# Odell "Vorpal Bunny" Dotson && Ethan "The Floorboards of Heaven" Prihar

import sys
import numpy
import random

data = []
inputArray = numpy.array([[0,0,1],
[0,1,1],
[1,0,1],
[1,1,1]])
outputArray = numpy.array([[0],[1],[1],[1]])
inputArrayFull = numpy.array([[0,0,1],
[0,1,1],
[1,0,1],
[1,1,1]])
outputArrayFull = numpy.array([[0],[1],[1],[1]])
numHiddenNodes = 0
holdOutPercent = 0

outputGuess = numpy.array([])
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

    global inputToHidden
    global hiddenToOutput

    inputToHidden = 2*numpy.random.random((int(inputSize),int(numHiddenNodes))) - 1
    hiddenToOutput = 2*numpy.random.random((int(numHiddenNodes),1)) - 1


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
    global inputToHidden
    global hiddenToOutput
    global outputGuess

    # propagate through the neural network by feeding forward
    sigV = numpy.vectorize(sig)
    sigDV = numpy.vectorize(sigD)

    hiddenValues = sigV(numpy.dot(inputArray,inputToHidden))
    outputGuess = sigV(numpy.dot(hiddenValues,hiddenToOutput))
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
    outputError = outputMisses * sigDV(outputGuess)
    #print outputError

    hiddenContribution = outputError.dot(hiddenToOutput.T)
    # This provides a weighted error
    hiddenError = hiddenContribution * sigDV(hiddenValues)

    # Update the weights:
    inputToHidden = inputArray.T.dot(hiddenError)
    hiddenToOutput = hiddenValues.T.dot(outputError)

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

#setup()
numHiddenNodes = sys.argv[2]
holdOutPercent = sys.argv[3]

random.seed(420) #None so that we use current system time.

inputSize = 2

global inputToHidden
global hiddenToOutput

inputToHidden = 2*numpy.random.random((3,int(numHiddenNodes))) - 1
hiddenToOutput = 2*numpy.random.random((int(numHiddenNodes),1)) - 1

print inputToHidden
print hiddenToOutput

backProp()
j=0
while(j < 100000):
    backProp()
    if(j%10000):
        global outputGuess
        print outputGuess
    j+=1
