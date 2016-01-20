package referee;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;


public class Player
{

	String playerName="Bulbasaur";
	BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	BoardTree playerBoard;
	int playerTurn; //Either a 1 or a 2, depending on if this player goes first or second respectively.
	int timeLimit; //The time limit for making a given move, in seconds.

	
	Player(String playerName, boolean first_move)
	{
		this.playerName = playerName;
	}
	
	
	/**
	 * This function sends the name of the player to system out where the referee with pick it up.
	 */
	public void sendName()
	{
		System.out.print(this.playerName);
	}
	
	
	/**
	 * This function reads the output from the refree when it tells us how the game is configured.
	 * This function also updates the playerBoard in player to use the given game configuration.
	 * 
	 * 
	 */
	public void readConfig() throws IOException
	{
		String inputData=input.readLine();	//These are sent as a one line separated with spaces.
		List<String> ls=Arrays.asList(inputData.split(" "));
		
		//Game information consists of 5 numbers [in this order]: 
		int height = Integer.parseInt(ls.get(0));//	 * board height (#rows), 
		int width = Integer.parseInt(ls.get(1));//	 * board width (#columns), 
		int N = Integer.parseInt(ls.get(2));//	 * number of pieces to win (the N in Connect-N), 
		int turn = Integer.parseInt(ls.get(3));//	 * turn of the player (1 indicating 1st player, and 2 indicating 2nd player
		int timeLimit = Integer.parseInt(ls.get(4));//	 * and the time limit to make a move in seconds
		//	 * Once the players receive these information, the game starts immediately. 
		
		this.playerTurn = turn;//Update the player to know who goes first based on config.
		this.timeLimit=timeLimit;//update the player's knowledge of the time limit.
		
		this.playerBoard = new BoardTree(new Board(height, width, N), null, turn, null, true);//Create the board with the given data from config.
	}
	
	
	/**
	 * Reads in a move touple from the refree of the form [move_operation move_location].
	 * Updates the playerBoard with that information.
	 */
	public void readMove() throws IOException
	{
		String inputData=input.readLine();	//These are sent as a one line separated with spaces.
		List<String> ls=Arrays.asList(inputData.split(" "));

		int location = Integer.parseInt(ls.get(0));
		int operation = Integer.parseInt(ls.get(1));
		this.playerBoard.update(location, operation); //Updates the board at the top of boardtree based on the move that was read.
	}
	
	
	/**
	 * Based on the player's current board, this function does the following:
	 * 		1. Creates a BoardTree with some ammount of possible steps forward, calculaing the heuristic for each board.
	 * 		2. Runs minimax on that tree replacing the heuristic values with the minimax values. TODO: With alpha beta pruning?
	 * 		3. From that tree, it decides which move to make.
	 * 
	 * @return move: The desired move we want to make in order to get to the desired next boardstate. 
	 */
	public void getNextMove()
	{
		//while we still have time,
		{
			playerBoard.makeChildren();
		}
		
		writeMove();
	}
	
	
	/**
	 * Tells the referee what our next move will be.
	 * NOTE that this function is also where we actually update the internal board, too. 
	 * We do this before we tell the referee our move to prevent getting yelled at.
	 */
	public void writeMove()
	{
		int location = this.playerBoard.move[0]; //TODO Is this the right move to access? Is this just null move?
		int operation = this.playerBoard.move[1];
		this.playerBoard.update(location, operation);
		String moveToWrite = "";
		moveToWrite.concat(Integer.toString(location));
		moveToWrite.concat(Integer.toString(operation));
 		System.out.print(moveToWrite);
	}
	
	
	public void processInput() throws IOException
	{	
    	String s=input.readLine();	
		List<String> ls=Arrays.asList(s.split(" "));
		if(ls.size()==2)
		{
			System.out.println(ls.get(0)+" "+ls.get(1));
		}
		else if(ls.size() == 1)
		{
			System.out.println("game over!!!");
			System.exit(0);
		}
		else if(ls.size() == 5) //ls contains game info
		{
			System.out.println("0 1");  //first move
		}
		else if(ls.size() == 4) //player1: aa player2: bb
		{		
			//TODO combine this information with game information to decide who is the first player
		}
		else
			System.out.println("not what I want");
	}
	
	
	public static void main(String[] args) throws IOException
	{
		Player rp = new Player(playerName, false);
		System.out.println(rp.playerName);
		while (true){
			rp.processInput();
		}

	}

}
