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

    It also splits it into the arrays of info that we will be learning on and what we will be testing on at the end.

    This function retrieves all the data from the specified text document and stores it in the global arrays.

    :param fileName: The name of the the file to get data from.
    """
    global inputArray
    global inputArrayFull
    global outputArray
    global outputArrayFull
    global inputArrayHeld
    global outputArrayHeld
    dataFile = open(fileName, 'r')
    numberOfLine = 0

    for line in dataFile:
        lineInfo = line.split(" ") #Split the line into into data points
        floatLineInfo = [] # Create a variable for when we (string -> float) them.
        for elt in lineInfo: #For each variable
            floatLineInfo.append(float(elt)) #Convert to float, add it to our data list.

        dataIn = [floatLineInfo[0], floatLineInfo[1]] # Store the data in from that line as dataIn
        dataOut = floatLineInfo[2] # Store the sanitized line info as dataOut for that line.

        if numberOfLine == 0: #if first time, create the array
            inputArrayFull = numpy.array((floatLineInfo[0], floatLineInfo[1]))
            outputArrayFull = numpy.array((floatLineInfo[2]))
        else: # If not firs tline, just vertaically stack the data.
            inputArrayFull = numpy.vstack((inputArrayFull, dataIn))
            outputArrayFull = numpy.vstack((outputArrayFull, dataOut))
        numberOfLine += 1

    dataFile.close()

    learningPortion = ((100.0-holdOutPercent)/100.0) # Converts this to a decimal value instead of a percent

    numLearn = 0
    numTest = 0

    for x in xrange(0, len(outputArrayFull)): # For all the data read in, split it into learning and testing.
        if x < int(len(outputArrayFull)*learningPortion): # If we are adding to our learning data set
            if numLearn == 0: # For the first time
                inputArray = numpy.array((inputArrayFull[x]))
                outputArray = numpy.array((outputArrayFull[x]))
            else: # Not the first time
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


def setup():
    """Sets up the system and retrieves data.

    This function calls getData to retrieve data and store it globally, as well as read in the
    number of hidden nodes and the percent of hold out that is specified by the user.

    Also does all the dealing with user specification of hidden nodes and holdout percentages.
    """
    global  numHiddenNodes
    global  holdOutPercent

    if len(sys.argv) == 2: # If we receive only two arguments, the program name and file name
        numHiddenNodes = 5 # default 5 hidden nodes
        holdOutPercent = 20 # default 20 holdout percent.
    elif len(sys.argv) == 4:
        if sys.argv[2] == 'h':
            numHiddenNodes = int(sys.argv[3])
            holdOutPercent = 20
        else:
            holdOutPercent = (100)*float(sys.argv[3])
            numHiddenNodes = 5
    else:
        numHiddenNodes = int(sys.argv[3])
        holdOutPercent = (100)*float(sys.argv[5])

    getData(sys.argv[1])

    numpy.random.seed([]) # Create a truly random seed every time based on system clock.

    inputSize = len(inputArrayFull[0])

    global inputToHiddenWeight
    global hiddenToOutputWeight

    print "Number of hidden nodes: ", numHiddenNodes
    print "Holdout percent: ", holdOutPercent, "%"

    inputToHiddenWeight = 2*numpy.random.random((int(inputSize),int(numHiddenNodes))) - 1
    hiddenToOutputWeight = 2*numpy.random.random((int(numHiddenNodes),1)) - 1


def sig(x):
    """ Gets the value of the sigmoid at x.
    """
    return 1.0/(1.0+numpy.exp(-x))


def sigD(x):
    """ Gets the derivative of a sigmoid at point x.
    """
    return x*(1.0-x)


def backProp():
    """
    Runs the backpropegation to learn from data and make predicitons.
    """
    global inputToHiddenWeight
    global hiddenToOutputWeight
    global outputGuess

    # propagate through the neural network by feeding forward
    sigV = numpy.vectorize(sig)
    sigDV = numpy.vectorize(sigD)

    hiddenValues = sig(numpy.dot(inputArray,inputToHiddenWeight))
    outputGuess = sig(numpy.dot(hiddenValues,hiddenToOutputWeight))

    outputMisses = outputArray - outputGuess # Calculating error
    outputError = outputMisses * sigD(outputGuess) # This provides a weighted error

    for i in xrange (0,len(outputGuess)):    # Here is where we round our output guesses because we are using classification
        if outputGuess[i] < .5:
            outputGuess[i] = 0
        else:
            outputGuess[i] = 1

    hiddenContribution = numpy.dot(outputError,hiddenToOutputWeight.T)
    # This provides a weighted error
    hiddenError = hiddenContribution * sigD(hiddenValues)

    inputToHiddenWeight += numpy.dot(inputArray.T,hiddenError) # Updates the synapse weights, so that we are actually
    hiddenToOutputWeight += numpy.dot(hiddenValues.T,outputError) # (con't) using back propogation for our guesses.


def nonBinHoldoutTest():
    """
    For nonbinary outputs, used only for fun and not this project.
    """
    global inputArray
    global outputArray
    global inputArrayHeld
    global outputArrayHeld
    inputArray = inputArrayHeld
    outputArray = outputArrayHeld
    backProp()

    total = len(outputArray)
    error = 0.0
    for i in range (0, total):
        #print "Actual output",outputArray[i]
        #print "Output guess",outputGuess[i]
        error += abs(outputArray[i] - outputGuess[i])
        #print "How wrong: ", abs(outputArray[i] - outputGuess[i])
    print "Avg. error percent:",  ((error / total) * 100.0)

def nonBinErrorPercent():
    """
    For nonbinary outputs. This checks the percent off that each datapoint is and averages how off they are.
    Used only for personal testing and not this actual project.
    """
    global inputArray
    global outputArray
    global inputArrayHeld
    global outputArrayHeld

    total = len(outputArray)
    error = 0.0
    for i in range (0, total):
        error += abs(outputArray[i] - outputGuess[i])
    return  (error / total) * 100.0

def holdoutTest():
    """
    Tests the trained neural net against the holdout data.
    """
    global inputArray
    global outputArray
    global inputArrayHeld
    global outputArrayHeld
    inputArray = inputArrayHeld
    outputArray = outputArrayHeld
    backProp()
    sys.stdout.write("The error when running on holdout data is " + str(calcErrorPercent()) + "%." '\n')


def calcErrorPercent():
    """
    Calculates the error percent against the actual given data.
    """
    global outputArray
    global outputGuess
    total = len(outputArray)
    error = 0.0
    for i in range (0, total):
        if outputArray[i] != outputGuess[i]:
            error += 1
    return error / total * 100.0


# #################################################################################################################### #
# #####################################################_MAIN_######################################################### #
# #################################################################################################################### #

setup() # Setup the neural network

for j in range (0, 3000): # Run for 3000 itterations
    backProp()
    if j%1000 == 0: # Update us on error rates every 1000 runs.
        print "Error percent after ", j, " runs is ", calcErrorPercent()

# Test the neural network on the holdout data
holdoutTest()