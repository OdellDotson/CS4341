package referee;
import java.util.ArrayList;

public class BoardTree
{
	Board board;
	BoardTree parent;
	ArrayList<BoardTree> children;
	int turn;
	int[] move;
	boolean oneCanPop;
	boolean twoCanPop;
	double cutoff;
	boolean pass;

	public BoardTree(Board board, BoardTree parent, int turn, int[] move, boolean oneCanPop, boolean twoCanPop)
	{
		this.board = board;
		this.parent = parent;
		children = new ArrayList<BoardTree>();
		this.turn = turn;
		this.move = move;
		this.oneCanPop = oneCanPop;
		this.twoCanPop = twoCanPop;
		if(turn == 1)
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
		if(children.isEmpty())
		{
			if(board.isConnectN() == -1)
			{
				int nextTurn = (turn == 1) ? 2 : 1;
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
		else
		{
			for(BoardTree child: children)
			{
				child.makeChildren();
			}
		}
	}

	public void update(int location, int opperation)
	{
		board.update(location, opperation, turn);
		if(opperation == 0)
		{
			if(turn == 1)
				oneCanPop = false;
			if(turn == 2)
				twoCanPop = false;
		}
		turn = (turn == 1) ? 2 : 1;
		move = null;
		children.clear();
		board.heuristic = 0.1;
	}

	public void makeTree(int depth)
	{
		for(int i=0; i<depth; i++)
		{
			makeChildren();
		}
	}

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
		int[] BADBADBAD = {100,100};
		return BADBADBAD;
	}
	
	public void pickFavoriteChild()
	{	
		if(turn == 1)
		{
			board.heuristic = -10000000;
			//System.out.println("Its player ones turn");
		}
		else
			board.heuristic = 10000000;
		for(BoardTree child: children)
		{
			//System.out.println("this should be called three times");
			if(child.board.heuristic == 0.1)
			{
				child.minimax();
				//System.out.println("this shouldnt be called at all");
			}
			if(pass && turn == 1 && child.board.heuristic > board.heuristic) // player 1 is maximizing
			{
				updateCutoff(child.board.heuristic);
				board.heuristic = child.board.heuristic;
				//System.out.println("this should happen once");
			}
			else if(pass && turn == 2 && child.board.heuristic < board.heuristic) // player 2 is minimizing
			{
				updateCutoff(child.board.heuristic);
				board.heuristic = child.board.heuristic;
				//System.out.println("this shouldnt be called at all");
			}
		}
	}
	
	public void updateCutoff(double value)
	{
		if(turn == 1) // alpha beta pruning for max
		{
			if(value > cutoff)
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
		if(parent != null)
		{
			parent.updateCutoff(value);
		}
	}

}
