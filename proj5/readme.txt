Odell Dotson and Ethan Prihar, Project 5 for CS4341
ocdotson@wpi.edu and ebprihar@wpi.edu

========================================================================================================================
Please note that this program is using

    Python 2.7.10
    Numpy library (for some added maths)

There are no additional external dependancies that do not come with python for our feature generation code to work.
========================================================================================================================
This code will take a set of inputs, defining the relationships between the items and the bags.

Our code will use the information given to create several classifications for each item, and then use backtracking and forward checking and heuristics to reorder the list and then solve the given constraint satisfaction problem.
========================================================================================================================
In order to run the program, first extract the archive ZIP file. Open a terminal and navigate to the extracted folder.
Once in the folder, run the command with the following format:


python main.py <desired file>



In order to specify a file to run the program on, look at the following examples:


python main.py input1.txt


is referring to your desired text file, named input1.txt in the same directory.
For example, this might look like:


python main.py input1.txt


Or, if your data is in a subdirectory:


python main.py data/input1.txt




This will print the solution to the terminal. Please note that the file extension AND directory need to be specified.
========================================================================================================================
For examples of verbose outputs, see the files also in this directory:

myoutput5.txt
myoutput7.txt
myoutput12.txt
myoutput20.txt
myoutput24.txt

The actual program supplied provides a much less messy output. If you’re interested in seeing these steps, uncomment the following lines in main:

65
67
76
92
101

as well as

line 34 in Bag.py
========================================================================================================================