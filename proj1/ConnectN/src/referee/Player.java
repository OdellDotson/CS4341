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
	
	public void sendName()
	{
		System.out.print(this.playerName);
	}
	
	public void readConfig()
	{
		BufferedReader inputData = this.input;
		this.playerBoard = new Board(inputData);
	}
	
	public void readMove()
	{
		moveRead; 
		//Read input from the referee about the oponent's move
		
		//Apply that information to our version of the board

		this.playerBoard.update(moveRead); //Updates the board based on the move that was read.
	}
	
	public void writeMove()
	{
		int[] move = {this.moveOperation, this.moveLocation};
 		System.out.print(move);
	}
	
	///////////////////////////
	//////////// TODO: This function goes in the constructor for boardTree, not in Player.
	public boardTree generateTree()
	{
		boardTree tree = new boardTree;
		
		//while not is connect n:
			//go through tree and create more nodes, more children, etc. 
		//Creates a tree of boards stemming from the current board.
		return tree;
	}
	//TODO: Move this function to the boardTree class.
	public boardTree minimaxTree(boardTree tree)
	//Given a tree, this function will run through it using Minimax and change the heuristic values of nonterminal nodes to the minimax value.
	{
		//In here is the alpha beta pruning
		return tree;
	}
	
	//TODO: Moe this to the boardTree class.
	public int[] findDesiredMove()
	{
		int[] move;
		move[0]
		return move;
	}
	
	public void getNextMove()
	{
		int[] move;//Create an array that will be populated by the move operation and move location.
		
		boardTree tree = new boardTree(playerBoard);//Creates the tree
		tree = tree.minimaxTree(tree); //Runs minimax on the generated tree, changing heuristic values into minimax values
		move = tree.findDesiredMove();
		
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
