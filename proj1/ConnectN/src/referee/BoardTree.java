package referee;
import java.util.ArrayList;

public class BoardTree
{
	Board board;
	BoardTree parent;
	ArrayList<BoardTree> children;
	int turn;
	int[] move;
	boolean canPop;

	public BoardTree(Board board, BoardTree parent, int turn, int[] move, boolean canPop)
	{
		this.board = board;
		this.parent = parent;
		children = new ArrayList<BoardTree>();
		this.turn = turn;
		this.move = move;
		this.canPop = canPop;
	}

	public void makeChildren()
	{
		if(children.isEmpty())
		{
			if(board.isConnectN() == -1)
			{
				int nextTurn = turn == 1 ? 2 : 1;
				for(int i=0;  i<board.width; i++)
				{
					if(board.canDropADiscFromTop(i,turn))
					{
						int[] childMove = {i, 1};
						children.add(new BoardTree(new Board(board, i, 1, turn), this, nextTurn, childMove, canPop));
					}
					if(canPop && board.canRemoveADiscFromBottom(i, 0))
					{
						int[] childMove = {i, 0};
						children.add(new BoardTree(new Board(board, i, 0, turn), this, nextTurn, childMove, false));
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
		children = new ArrayList<BoardTree>();
	}

	public void pickFavoriteChild()
	{
		long bestHeuristic = children.get(0).board.heuristic;
		for(BoardTree i: children)
		{
			if(turn == 1 && i.board.heuristic > bestHeuristic) // player 1 is maximizing
				bestHeuristic = i.board.heuristic;
			else if(i.board.heuristic < bestHeuristic) // player 2 is minimizing
			{
				bestHeuristic = i.board.heuristic;
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

}