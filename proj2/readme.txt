Odell Dotson and Ethan Prihar, Neural Network assignment for CS4341

========================================================================================================================
Please note that this implementation of a neural network is using:

    Python 2.7.10
    Numpy library

(Note that numpy as an external library is a required resource for this implementation to work.)
========================================================================================================================

In order to run the neural network, please first open a terminal of your choice. Unzip the provided archive, and navigate
to the unzipped documents in terminal.

To run the neural network, enter the commands in the following form:

python ann.py <filename> [h <number of hidden nodes> | p <holdout percentage> ]

where filename is a set of datapoints of the form:

<x input> <y input> <associated output>


Note that the holdout percentage is given as a decimal when a command is called.
========================================================================================================================
Examples (as provided in the project description):

input:  python ann.py hwk5data.txt h 8 p 0.1
behavior: the program should run with 8 hidden nodes and hold out 10 percent of the data for testing
-----------------------------------------------------
input:  python ann.py hwk5data.txt h 8
behavior: the program should run with 8 hidden nodes and the default value of 20 percent for the amount of data withheld for testing
-----------------------------------------------------
input:  python ann.py hwk5data.txt p 0.1
behavior: the program should run with the default value of 5 hidden nodes and hold out 10 percent of the data for testing
-----------------------------------------------------
input:  python ann.py hwk5data.txt
behavior: the program should run with the default value of 5 hidden nodes and hold out the default value of 20 percent of the data for testing



Number three:
3.(10 points) Discuss any simplifying assumptions that you made while implementing the neural network.
How resistant would your implementation be to changes in the number of input nodes? hidden layers? output nodes? network topology?

