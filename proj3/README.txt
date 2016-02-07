Odell Dotson and Ethan Prihar, Project 3 for CS4341
ocdotson@wpi.edu and ebprihar@wpi.edu

========================================================================================================================
Please note that this program is using

    Python 2.7.10

There are no additional external dependancies for our feature generation code to work.
========================================================================================================================
This code will take a set of 43 inputs, 1-42 defining a board state and 43 giving the eventual winner of that board.

Our code will use the information given to create several classifications for each board state, and write to a new file
with the classification information.
========================================================================================================================
In order to run the classification program, first extract the archive ZIP file. Open a terminal and navigate to the extracted folder.
Once in the folder, run the command with the following format:

python generateFeatures.py <input file name> <output file name>


This will generate a new file called <output file name> and in that file, add a row of columns to the far right edge that are our features 1-5.
Note that it does not rearrange the winner column. Out code simply adds an additional 5 columns, or an additional 5 coma separated values to 
each line. 
========================================================================================================================
Please note that YOU AS USER need to specify that you are GIVING and EXPECT .csv files.

GOOD:   python generateFeatures.py input.csv output.cvs
BAD:    python generateFeatures.py input output
========================================================================================================================