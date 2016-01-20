package referee;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;


public class Player
{

	String playerName="aa";
	BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	boolean first_move=false;
	Board playerBoard;
	int moveOperation;
	int moveLocation;
	
	Player(String playerName, boolean first_move)
	{
		this.playerName = playerName;
		this.first_move = first_move;
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
	 * TODO: Test reading in from the buffer.
	 * TODO: Make it actually create the new board correctly from those inputs.
	 */
	public void readConfig()
	{
		BufferedReader inputData = this.input;
		this.playerBoard = new Board(inputData);
	}
	
	/**
	 * Reads in a move touple from the refree of the form [move_operation move_location].
	 * Updates the playerBoard with that information.
	 */
	public void readMove()
	{
		BufferedReader inputData = this.input;
		//Read input from the referee about the oponent's move
		
		//Apply that information to our version of the board

		this.playerBoard.update(moveRead); //Updates the board based on the move that was read.
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
		int[] move;//Create an array that will be populated by the move operation and move location.
		
		BoardTree tree = new BoardTree(playerBoard);//Creates the tree
		tree = tree.minimaxTree(tree); //Runs minimax on the generated tree, changing heuristic values into minimax values
		move = tree.findDesiredMove();
	}
	
	/**
	 * Tells the referee what our next move will be.
	 * NOTE that this function is also where we actually update the internal board, too. We do this before we tell the referee our move.
	 */
	public void writeMove()
	{
		playerBoard.update(this.moveOperation, this.moveLocation);
		int[] move = {this.moveOperation, this.moveLocation};
 		System.out.print(move);
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
		Player rp = new Player();
		System.out.println(rp.playerName);
		while (true){
			rp.processInput();
		}

	}

}
