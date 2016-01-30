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

    for line in dataFile:
        lineInfo = line.split(" ") #Split the line into into data points
        floatLineInfo = [] # Create a variable for when we (string -> float) them.
        for elt in lineInfo: #For each variable
            floatLineInfo.append(float(elt))

        dataIn = [floatLineInfo[0], floatLineInfo[1]] # Store the data in from that line as dataIn
        dataOut = floatLineInfo[2] # Store the sanitized line info as dataOut for that line.

        if numberOfLine == 0:
            inputArrayFull = numpy.array((floatLineInfo[0], floatLineInfo[1]))
            outputArrayFull = numpy.array((floatLineInfo[2]))
        else:
            inputArrayFull = numpy.vstack((inputArrayFull, dataIn))
            outputArrayFull = numpy.vstack((outputArrayFull, dataOut))
        numberOfLine += 1

    #print inputArrayFull
    #print outputArrayFull

    dataFile.close()

    learningPortion = ((100.0-holdOutPercent)/100.0) # Converts this to a decimal value instead of a percent

    numLearn = 0
    numTest = 0
    print outputArrayFull

    for x in xrange(0, len(outputArrayFull)):
        if(x < int(len(outputArrayFull)*learningPortion)): # If we are adding to our learning data set
            if numLearn == 0: # For the first time
                inputArray = numpy.array((inputArrayFull[x]))
                outputArray = numpy.array((outputArrayFull[x]))
                print outputArray
            else: # Not the first rodeo
                xVal,yVal=inputArrayFull[x]
                dataIn = numpy.array((xVal,yVal))
                dataOut = outputArrayFull[x]
                inputArray = numpy.vstack((inputArray, dataIn))
                outputArray = numpy.vstack((outputArray, dataOut))
            numLearn +=1
        else: # If we are adding to our testing data set
            if numTest == 0: # for the first time
                inputArrayHeld = numpy.array((inputArrayFull[x]))
                outputArrayHeld = numpy.array((outputArrayFull[x]))
            else: # not first time
                xVal,yVal= inputArrayFull[x]
                dataIn = numpy.array((xVal,yVal))
                dataOut = outputArrayFull[x]
                inputArrayHeld = numpy.vstack((inputArrayHeld, dataIn))
                outputArrayHeld = numpy.vstack((outputArrayHeld, dataOut))
            numTest+=1

    print "Populated input array: ", inputArray
    print "Populated output array: ", outputArray


def setup():
    """Sets up the system and retrieves data.

    This function calls getData to retrieve data and store it globally, as well as read in the
    number of hidden nodes and the percent of hold out that is specified by the user.
    """
    global  numHiddenNodes
    global  holdOutPercent

    numHiddenNodes = float(sys.argv[2])
    holdOutPercent = float(sys.argv[3])

    getData(sys.argv[1])

    random.seed(420) #None so that we use current system time.

    print "Hold up"
    inputSize = len(inputArrayFull[0])

    print "Input size: " , inputSize
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
    #print "------------------------------------------------------------------------------------------"

    """for i in xrange (0,len(outputGuess)):
        if outputGuess[i] < .5:
            outputGuess[i] = 0
        else:
            outputGuess[i] = 1"""
    # Calculating error:
    outputMisses = outputArray - outputGuess
    #print "output guess-----------"
    #print outputGuess

    #print "--------------Output misses:"
    #print outputMisses
    # This provides a weighted error
    outputError = (1.0)*outputMisses * sigD(outputGuess)
    #print "Output errors:------------"
    #print outputError

    hiddenContribution = numpy.dot(outputError,hiddenToOutputWeight.T)
    # This provides a weighted error
    hiddenError = hiddenContribution * sigD(hiddenValues)

    # Update the weights:
    #print "----------------Old input -> hidden weights:--------------------------------------------------------"
    #print inputToHiddenWeight
    #print "----------------------New input -> hidden weights:-------------------------------------------------------"
    inputToHiddenWeight += numpy.dot(inputArray.T,hiddenError)
    hiddenToOutputWeight += numpy.dot(hiddenValues.T,outputError)
    #print inputToHiddenWeight
    #print "---------------------Re itterate-------------------------------------------------------"


def calcErrorPercent():
    total = len(outputArray)
    error = 0.0
    for i in range (0, total):
        if outputArray[i] != outputGuess[i]:
            error += 1
    return error / total * 100.0

def holdoutTestVerbose():
    global inputArray
    global outputArray
    global inputArrayHeld
    global outputArrayHeld
    inputArray = inputArrayHeld
    outputArray = outputArrayHeld
    backProp()

    #print "Input array:",inputArray
    #print "Output array", outputArray

    total = len(outputArray)
    #print "Total: ",total
    error = 0.0
    for i in range (0, total):
        #print "Actual output",outputArray[i]
        #print "Output guess",outputGuess[i]
        error += abs(outputArray[i] - outputGuess[i])
        #print "How wrong: ", abs(outputArray[i] - outputGuess[i])
    print "Avg. error percent:",  ((error / total) * 100.0)

def errorPercent():
    global inputArray
    global outputArray
    global inputArrayHeld
    global outputArrayHeld
    backProp()

    total = len(outputArray)
    error = 0.0
    for i in range (0, total):
        error += abs(outputArray[i] - outputGuess[i])
    return  ((error / total) * 100.0)

def holdoutTest():
    global inputArray
    global outputArray
    global inputArrayHeld
    global outputArrayHeld
    inputArray = inputArrayHeld
    outputArray = outputArrayHeld
    backProp()
    print "The error is: ", calcErrorPercent()



# #################################################################################################################### #
# #####################################################_MAIN_######################################################### #
# #################################################################################################################### #

setup()


print inputArray
print outputArray

backProp()

#while(calcErrorPercent() > 10):
    #backProp()

for j in range (0, 50001):
    backProp()
    if j%10000 == 0:
        print "Error percent on run number " , j, " is: ",errorPercent()


# Test the neural network on the holdout data
holdoutTestVerbose()