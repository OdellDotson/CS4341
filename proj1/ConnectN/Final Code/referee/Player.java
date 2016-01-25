/**
 * This code is created for cs 4341 AI 2013a at WPI. All rights are reserved. 
 * Code was provided by course staff and modified by Odell Dotson and Ethan Prihar
 * ocdotson@wpi.edu && ebprihar@wpi.edu
 */
package referee;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;


public class Player
{

	String playerName;//The string that is given as player name to the refree when asked.
	BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	BoardTree playerBoard;
	int playerTurn; //Either a 1 or a 2, depending on if this player goes first or second respectively.
	int timeLimit; //The time limit for making a given move, in seconds.

	/**
	 * Simple constructor for the player class, only requiring a name.
	 */
	public Player(String playerName)
	{
		this.playerName = playerName;
	}
	
	
	/**
	 * This function sends the name of the player to system out where the referee with pick it up.
	 */
	public void sendName()
	{
		System.out.println(this.playerName);
	}
	
	
	/**
	 * This function reads the output from the refree when it tells us how the game is configured.
	 * This function also updates the playerBoard in player to use the given game configuration.
	 * 
	 * @params ls: ls is the list of strings, in List form, given by the refree about the config.
	 */
	public void readConfig(List<String> ls) throws IOException
	{
		//Game information consists of 5 numbers [in this order]: 
		int height = Integer.parseInt(ls.get(0));//	 * board height (#rows), 
		int width = Integer.parseInt(ls.get(1));//	 * board width (#columns), 
		int N = Integer.parseInt(ls.get(2));//	 * number of pieces to win (the N in Connect-N), 
		int turn = Integer.parseInt(ls.get(3));//	 * turn of the player (1 indicating 1st player, and 2 indicating 2nd player
		int timeLimit = Integer.parseInt(ls.get(4));//	 * and the time limit to make a move in seconds
		//	 * Once the players receive these information, the game starts immediately. 
		
		this.timeLimit=timeLimit;//update the player's knowledge of the time limit.
		
		this.playerBoard = new BoardTree(new Board(height, width, N), null, turn, null, true, true);//Create the board with the given data from config.
	}
	
	
	/**
	 * Reads in a move touple from the refree of the form [move_operation move_location].
	 * Updates the playerBoard with that information.
	 */
	public void readMove(List<String> ls) throws IOException
	{
		int location = Integer.parseInt(ls.get(0));
		int operation = Integer.parseInt(ls.get(1));
		playerBoard.update(location, operation); //Updates the board at the top of boardtree based on the move that was read.
	}
	
	
	
	/**
	 * Tells the referee what our next move will be.
	 * NOTE that this function is also where we actually update the internal board, too. 
	 * We do this before we tell the referee our move to prevent getting yelled at.
	 */
	public void writeMove(int location, int operation)
	{
		this.playerBoard.update(location, operation);
 		System.out.println("" + location + " " + operation);
	}
	
	/**
	 * 
	 */
	public void processInput() throws IOException
	{	
    	String s=input.readLine();	
		List<String> ls=Arrays.asList(s.split(" "));
		if(ls.size()==2)
		{
			readMove(ls);
			if(playerBoard.turn == playerTurn)
			{
				play();
			}
		}
		else if(ls.size() == 1)
		{
			System.out.println("game over!!!");
			System.exit(0);
		}
		else if(ls.size()==4)
		{
			if(ls.get(1).equals(playerName))
			{
				playerTurn = 1;
			}
			else
			{
				playerTurn = 2;
			}
		}
		else if(ls.size() == 5) //ls contains game info
		{
			readConfig(ls);
			if(playerBoard.turn == playerTurn)
			{
				play();
			}
		}
	}
	
	public void play()
	{
		if(playerBoard.turn == playerTurn)
		{
			if(timeLimit <= 2) // taking into account how many seconds we have
				playerBoard.makeTree(4);
			else if(timeLimit <= 10)
				playerBoard.makeTree(6);
			else
				playerBoard.makeTree(7);
			playerBoard.makeHeuristic(); // makes the heuristics
			int[] move = playerBoard.minimax(); // determines the best move
			writeMove(move[0], move[1]); // publishes the move
		}
	}
	
	public static void main(String[] args) throws IOException
	{
		Player rp = new Player("SHSHHWHWHHWHW");
		rp.sendName();
		while (true)
		{
			rp.processInput();
		}
		
		//TESTING STUFF
		/*
		rp.playerBoard = new BoardTree(new Board(6, 7, 4), null, 1, null, true, true);
		for(int i = 0; i < 50; i++)
		{
			if(rp.playerBoard.board.isConnectN() == -1)
			{	
				rp.playerBoard.makeTree(2);
				rp.playerBoard.makeHeuristic();
				System.out.println("TOP TREE");
				rp.playerBoard.board.printBoard();
				System.out.println(rp.playerBoard.board.heuristic);
				System.out.println("NEXT LAYER");
				for(BoardTree child: rp.playerBoard.children)
				{
					child.board.printBoard();
					System.out.println(child.board.heuristic);
					System.out.println("" + child.move[0] + " " + child.move[1]);
				}
				System.out.println("NEXT LAYER");
				for(BoardTree child: rp.playerBoard.children)
				{
					for(BoardTree child2: child.children)
					{
						child2.board.printBoard();
						System.out.println(child2.board.heuristic);
						System.out.println("" + child2.move[0] + " " + child2.move[1]);
					}
				}
				int[] move = rp.playerBoard.minimax();
				System.out.println("AFTER MINMAX");
				System.out.println("TOP TREE");
				rp.playerBoard.board.printBoard();
				System.out.println(rp.playerBoard.board.heuristic);
				System.out.println("NEXT LAYER");
				for(BoardTree child: rp.playerBoard.children)
				{
					child.board.printBoard();
					System.out.println(child.board.heuristic);
					System.out.println("" + child.move[0] + " " + child.move[1]);
				}
				System.out.println("NEXT LAYER");
				for(BoardTree child: rp.playerBoard.children)
				{
					for(BoardTree child2: child.children)
					{
						child2.board.printBoard();
						System.out.println(child2.board.heuristic);
						System.out.println("" + child2.move[0] + " " + child2.move[1]);
					}
				}
				rp.playerBoard.update(move[0],move[1]);
				System.out.println("THE MOVE TO MAKE IS: ");
				System.out.println("" + move[0] + " " + move[1]);
			}
			else
				System.exit(0);
		}
		*/
	}

}
