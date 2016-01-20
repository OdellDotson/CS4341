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
		for(int i=0; i++; i<board.width)
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

	/**
	 * Given a tree, this function will run through it using Minimax and change the heuristic values of nonterminal nodes to the minimax value.
	 * 
	 * @param tree: The BoardTree that we will run minimax on.
	 * @return tree: Return the tree with minimax performed on it.
	 */
	public BoardTree minimaxTree(BoardTree tree)
	{
		//In here is the alpha beta pruning
		return tree;
	}
	
	/**
	 * 
	 * @return
	 */
	public int[] findDesiredMove()
	{
		int[] move;
		move[0]
		return move;
	}
}
