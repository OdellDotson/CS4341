CS4341 Introduction to Artificial Intelligence
Project 1 - ConnectN

Authors:
Ethan Prihar
Odell Dotson


INTRODUCTION
------------
This project was to create an AI using ID-DFS, Alpha-beta pruning and minimax algorithm to play ConnectN. The shown code interfaces with a referee, receiving the opponents moves only through that referee. Moves are communicated through the standard System.out. 


RUNNING
-------
here are three sourcecode files supplied:

Board.java
BoardTree.java
Player.java

We have provided a compiled Player.jar file for your convenience, but if you would like to recompile it from our provided sourcecode that is also file. 

Using whatever program you'd like, such as Eclipse, compile Player.java into an executable jar. Ensure that the Player.java file is the one whose main function is being used.

In order to run our AI, use the following command in terminal:

java -jar C:\path\to\Referee.jar "java -jar C:\path\to\Player.jar" "java -jar C:\path\to\Opponent.jar" 6 7 3 10 10


This will run our player against an opponent player, using the supplied referee as intermediary.
