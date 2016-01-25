// This code was made by Ethan Prihar and Odell Dotson

package referee;
import java.util.ArrayList;

public class BoardTree
{
	Board board; // the board of connect n
	BoardTree parent; // the boards parent board
	ArrayList<BoardTree> children; // all of the boards that could be made by making a move on this board
	int turn; // whos turn it is to play on this board
	int[] move; // the move that lead you from the parent board to this board
	boolean oneCanPop; // if player one can pop a piece
	boolean twoCanPop; // if player 2 can pop a piece
	double cutoff; // the alpha beta pruning cutoff value
	boolean pass; // whether or not the branch has been pruned

	public BoardTree(Board board, BoardTree parent, int turn, int[] move, boolean oneCanPop, boolean twoCanPop)
	{
		this.board = board;
		this.parent = parent;
		children = new ArrayList<BoardTree>();
		this.turn = turn;
		this.move = move;
		this.oneCanPop = oneCanPop;
		this.twoCanPop = twoCanPop;
		if(turn == 1) // start off with very low or very high cutoff value so that it is immidiatly overridden
			cutoff = -2147483648;
		else
			cutoff = 2147483647;
		pass = true;
	}

	/**
	* This function will create children for any element in a tree that doent have children
	* and isn't and end condition
	*/
	public void makeChildren() 
	{
		if(children.isEmpty())  // if this boardTree object has no children, make it children
		{
			if(board.isConnectN() == -1)
			{
				int nextTurn = (turn == 1) ? 2 : 1;  // this switches the turn so we know whos turn is next
				for(int i=0;  i<board.width; i++)
				{
					if(board.canDropADiscFromTop(i,turn))
					{
						int[] childMove = {i, 1};
						children.add(new BoardTree(new Board(board, i, 1, turn), this, nextTurn, childMove, oneCanPop, twoCanPop));
					}
					if(turn == 1 && oneCanPop && board.canRemoveADiscFromBottom(i, 0))
					{
						int[] childMove = {i, 0};
						children.add(new BoardTree(new Board(board, i, 0, turn), this, nextTurn, childMove, false, twoCanPop));
					}
					else if(turn == 2 && twoCanPop && board.canRemoveADiscFromBottom(i, 0))
					{
						int[] childMove = {i, 0};
						children.add(new BoardTree(new Board(board, i, 0, turn), this, nextTurn, childMove, oneCanPop, false));
					}
				}
			}
		}
		else // if it already has children make children for it's children
		{
			for(BoardTree child: children)
			{
				child.makeChildren();
			}
		}
	}

	// this function updates the BoardTree when a move has been made
	public void update(int location, int opperation)
	{
		board.update(location, opperation, turn); // updates the board
		if(opperation == 0)
		{
			if(turn == 1)
				oneCanPop = false;
			if(turn == 2)
				twoCanPop = false;
		}
		turn = (turn == 1) ? 2 : 1;
		move = null; // clears the children and move so more minmax can be done
		children.clear();
		board.heuristic = 0.1;
	}
 
 	// creates a tree of given depth
	public void makeTree(int depth)
	{
		for(int i=0; i<depth; i++)
		{
			makeChildren();
		}
	}

	// this fucntion calls the make heruistic class on the bottom layer of the tree for minmax purposes
	public void makeHeuristic()
	{
		if(children.isEmpty())
		{
			board.makeHeuristic();
		}
		else
		{
			for(BoardTree child: children)
			{
				child.makeHeuristic();
			}
		}
	}
	
	
	// this fucntion does the minmax algorithm
	public int[] minimax()
	{
		if(board.heuristic == 0.1) // dont have a heuristic and you have kids
		{
			//System.out.println("Minimax is called");
			pickFavoriteChild();
		}
		for(BoardTree child: children) // this finds the move to the best option
		{
			if(this.board.heuristic == child.board.heuristic)
			{
				return child.move;
			}
		}
		int[] BADBADBAD = {100,100}; // this is never returned
		return BADBADBAD;
	}
	
	// this function picks the best heuristic value of all the boards children and makes it the boards heuristic
	public void pickFavoriteChild()
	{	
		// sets values to start very high or low so that it will be overridden quickly
		if(turn == 1)
		{
			board.heuristic = -10000000;
			//System.out.println("Its player ones turn");
		}
		else
			board.heuristic = 10000000;
		for(BoardTree child: children) // for every child
		{
			if(child.board.heuristic == 0.1) // if the child doesnt have a heruristic, run minmax on it to give it one
			{
				child.minimax();
			}
			if(pass && turn == 1 && child.board.heuristic > board.heuristic) // player 1 is maximizing
			{
				updateCutoff(child.board.heuristic); // this does alpha beta pruning
				board.heuristic = child.board.heuristic; // this picks the max value for maxing
			}
			else if(pass && turn == 2 && child.board.heuristic < board.heuristic) // player 2 is minimizing
			{
				updateCutoff(child.board.heuristic);  // this does alpha beta pruning
				board.heuristic = child.board.heuristic; // this picks the min value for mining
			}
		}
	}
	
	// this function does alpha beta pruning by checking if the heuristic of a node
	// is beyond the cutoff value of a parent node and if it is, setting the node to
	// pass = false, which stops minmax from exploring it
	// this fucntion also carrys cutoff values up the chain of parents to the first node

	public void updateCutoff(double value)
	{
		if(turn == 1) // alpha beta pruning for max
		{
			if(value > cutoff)
			{
				cutoff = value;
			}
			else if(!(children.isEmpty())) // if you have kids
			{
				for(BoardTree child: children) // find which kid is not worth minmaxing
				{
					if(child.cutoff == value)
					{
						child.pass = false; // make it not passable
					}
				}
			}
		}
		else // alpha beta pruning for min
		{
			if(value < cutoff)
			{
				cutoff = value;
			}
			else if(!(children.isEmpty()))
			{
				for(BoardTree child: children)
				{
					if(child.cutoff == value)
					{
						child.pass = false;
					}
				}
			}
		}
		if(parent != null) // if you have a parent, pass them the cutoff value too
		{
			parent.updateCutoff(value);
		}
	}

}
