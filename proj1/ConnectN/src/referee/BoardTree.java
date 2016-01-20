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

	public void update(int location, int opperation)
	{
		board.update(location, opperation, turn);
		children = new ArrayList<BoardTree>();
	}

	public void pickFavoriteChild()
	{
		int bestHeuristic = children.get(0).board.heuristic;
		for(BoardTree i: children)
		{
			if(turn == 1 && i.board.heuristic > bestHeuristic) // player 1 is maximizing
				bestHeuristic == i.board.heuristic;
			else if(i.board.heuristic < bestHeuristic) // player 2 is minimizing
			{
				bestHeuristic == i.board.heuristic;
			}
		}
		board.heruistic = bestHeuristic;
	}

	public int[] minimax()
	{
		if(parent == null)
		{
			pickFavoriteChild();
			for(BoardTree i: children)
			{
				if(i.board.heuristic == board.heuristic)
					return i.move;
			}

		}
	}
	

}
