Odell Dotson and Ethan Prihar, Project 6 for CS4341
ocdotson@wpi.edu and ebprihar@wpi.edu

========================================================================================================================
Please note that this program is using

    Python 2.7.10
    Python’s “random” library 

There are no additional external dependancies that do not come with python for our feature generation code to work.
========================================================================================================================
This code will take in two files and a specification for either n runs mode or convergence mode.

We have selected Option B for this project.
========================================================================================================================
When the program is run, it will be in one of two modes, either run-n-times mode or convergence mode.

If it is simply to run through rejection sampling and likelihood weighting n times, the output would look something like this:

Rejection sampling:  0.470760846783
Likelihood weighting:   0.471738331694

If error convergence testing is used, the output would look something like this:

Runs for rejection sampling:  4630.0
Rejection sampling with convergence:  0.462850971922
Runs for likelihood weighting:  3136
Likelihood weighting with convergence:   0.471321695761

The code as provided converges the error to less than .0001 between two different calculations. The code also prints how many runs
it took for each to reach that convergence. .0001 was selected because we were not given a value, and experimentally this provided decent
approximations very quickly. 
========================================================================================================================
In order to run the program, first extract the archive ZIP file. Open a terminal and navigate to the extracted folder.
Once in the folder, run the command with the following format:


python main.py <desired network config file> <desired query file> <n>

Desired network config file is a file conforming to the structure in Option B’s form, describing a Bayesian network.

The desired query file is a file that gives the code the query variable and any given evidence variables. 

n is a selection between two different modes.



If you want to run the code to do 10,000 iterations of rejection sampling and likelihood weighting, then n would be 10000
and the command would look like:

python main.py network_option_b.txt query1.txt 10000


If you wanted to test how quickly rejection sampling and likelihood weighting converge, then you would give n = -1:

python main.py network_option_b.txt query1.txt -1



This will print the solution to the terminal. Please note that the file extensions MUST be specified.
========================================================================================================================