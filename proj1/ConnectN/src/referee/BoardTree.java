package referee;

public class BoardTree
{
	Board currentState;
	BoardTree parent;
	List<BoardTree> children;
	int turn;
	String move;
	boolean pop;

	public BoardTree(Board currentState, BoardTree parent, int turn, String move, boolean pop)
	{
		this.currentState = currentState;
		this.parent = parent;
		children = new ArrayList<BoardTree>();
		this.turn = turn;
		this.move = move;
		this.pop = pop;	
	}

	/**
	 * 
	 * @return
	 */
	public void makeChildren()
	{
		//while not is connect n:
		//go through tree and create more nodes, more children, etc. 
		//Creates a tree of boards stemming from the current board.
		return tree;
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
