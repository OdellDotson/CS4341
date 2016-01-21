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

	public BoardTree(Board board, BoardTree parent, int turn, int[] move, boolean oneCanPop, boolean twoCanPop)
	{
		this.board = board;
		this.parent = parent;
		children = new ArrayList<BoardTree>();
		this.turn = turn;
		this.move = move;
		this.oneCanPop = oneCanPop;
		this.twoCanPop = twoCanPop;
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
		children = new ArrayList<BoardTree>();
	}

	public void pickFavoriteChild(int depth)
	{
		long bestHeuristic = children.get(0).board.heuristic;
		for(BoardTree child: children)
		{
			if(child.board.heuristic == 2147483646)
			{
				child.minimax(depth);
			}
			if(turn == 1 && child.board.heuristic > bestHeuristic) // player 1 is maximizing
			{
				bestHeuristic = child.board.heuristic;
			}
			else if(child.board.heuristic < bestHeuristic) // player 2 is minimizing
			{
				bestHeuristic = child.board.heuristic;
			}
		}
		board.heuristic = bestHeuristic;
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

	public int[] minimax(int depth)
	{
		makeTree(depth);
		makeHeuristic();
		if(board.heuristic == 2147483646)
		{
			parent.pickFavoriteChild(depth);
		}
		else
		{
			for(BoardTree child: children)
			{
				child.minimax(depth);
			}
		}
		for(BoardTree child: children)
		{
			if(this.board.heuristic == child.board.heuristic)
			{
				return child.move;
			}
		}
		System.out.println("PROBLEM");
		int[] BADBADBAD = {0,0};
		return BADBADBAD;
	}

}
