package referee;
import java.util.ArrayList;

public class BoardTree
{
	Board board;
	BoardTree parent;
	ArrayList<BoardTree> children;
	int turn;
	int[] move;
	boolean 1CanPop;
	boolean 2CanPop;

	public BoardTree(Board board, BoardTree parent, int turn, int[] move, boolean 1CanPop, boolean 2CanPop)
	{
		this.board = board;
		this.parent = parent;
		children = new ArrayList<BoardTree>();
		this.turn = turn;
		this.move = move;
		this.1CanPop = 1CanPop;
		this.2CanPop = 2CanPop;
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
						children.add(new BoardTree(new Board(board, i, 1, turn), this, nextTurn, childMove, 1canPop, 2CanPop));
					}
					if(turn == 1 && 1CanPop && board.canRemoveADiscFromBottom(i, 0))
					{
						int[] childMove = {i, 0};
						children.add(new BoardTree(new Board(board, i, 0, turn), this, nextTurn, childMove, false, 2CanPop));
					}
					else if(turn == 2 && 2CanPop && board.canRemoveADiscFromBottom(i, 0))
					{
						int[] childMove = {i, 0};
						children.add(new BoardTree(new Board(board, i, 0, turn), this, nextTurn, childMove, 1CanPop, false));
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
		turn = (turn == 1) ? 2 : 1;
		if(opperation == 0)
		{
			canPop = false;
		}
		move = null;
		children = new ArrayList<BoardTree>();
	}

	public void pickFavoriteChild()
	{
		long bestHeuristic = children.get(0).board.heuristic;
		for(BoardTree child: children)
		{
			if(child.board.heuristic == null)
			{
				child.minimax();
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

	public int[] minimax()
	{
		makeTree();
		makeHeuristic();
		if(board.heruistic != null)
		{
			parent.pickFavoriteChild();
		}
		else
		{
			for(BoardTree child: children)
			{
				child.minimax();
			}
		}
		for(BoardTree child: children)
		{
			if(this.board.heruistic == child.board.heuristic)
			{
				return child.move;
			}
			else
			{
				System.out.println("PROBLEM");
				return {0,0};
			}
		}
	}

}
