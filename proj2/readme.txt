How to run:

Open a terminal.

Enter the command:

python ann.py <filename> [h <number of hidden nodes> | p <holdout percentage> ]


Examples:

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



Note that the holdout percentage is given as a decimal.