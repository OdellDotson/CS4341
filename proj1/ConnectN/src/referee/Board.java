/**
 * This code is created for cs 4341 AI 2013a at WPI. All rights are reserved. 
 */
package referee;

/**
 * @author lzhu
 *
 */
public class Board {
	
	int width;
	int height;
	int board[][];
	int numOfDiscsInColumn[];
	int emptyCell=9;
	int N;
	long heuristic = 2147483646;
	int PLAYER1=1;
	int PLAYER2=2;
	int NOCONNECTION=-1;
	int TIE=0;
	
	 Board(int height, int width, int N)
	 {
		this.width=width;
		this.height=height;
		board =new int[height][width];
		for(int i=0;i<height;i++)
			for(int j=0;j<width;j++){
				board[i][j]=this.emptyCell;
			}
		numOfDiscsInColumn = new int[this.width];
		this.N=N;
	 }

	//contructor that makes a copy of a board and updates it too.
	Board(Board old, int location, int opperation, int player)
	{
		this.width = old.width;
		this.height = old.height;
		this.board = old.board;
		this.numOfDiscsInColumn = old.numOfDiscsInColumn;
		this.update(location, opperation, player);
	}
	 
	 public void printBoard(){
		 System.out.println("Board: ");
		 for(int i=0;i<height;i++){
				for(int j=0;j<width;j++){
					System.out.print(board[i][j]+" ");
				}
				System.out.println();
		 }
	 }

	public void update(int location, int opperation, int player)
	{
		if(opperation == 1)
		{
			dropADiscFromTop(location, player);
		}
		else
		{
			removeADiscFromBottom(location);
		}
	}
	 
	 public boolean canRemoveADiscFromBottom(int col, int currentPlayer){
		 if(col<0 || col>=this.width) {
			 System.out.println("Illegal column!");
			 return false;
			 }
		 else if(board[height-1][col]!=currentPlayer){
			 System.out.println("You don't have a checker in column "+col+" to pop out!");
			 return false;
		 }
		 else 
			 return true;
	 }
	 
	 
	 
	 public void removeADiscFromBottom(int col){
		 int i;
		 for(i=height-1;i>height-this.numOfDiscsInColumn[col];i--){
			 board[i][col]=board[i-1][col];
		 }
		 board[i][col]=this.emptyCell;
		 this.numOfDiscsInColumn[col]--;
	 }
	 
	 
	 public boolean canDropADiscFromTop(int col, int currentPlayer){
		 if(col<0 || col>=this.width) {
			 System.out.println("Illegal column!");
			 return false;
			 }
		 else if(this.numOfDiscsInColumn[col]==this.height){
			 System.out.println("Column is already full. Cannot drop more disc in it.");
			 return false;
		 }
		 else
			 return true;
	 }
	 
	 public void dropADiscFromTop(int col, int currentplayer){
		 int firstEmptyCellRow=height-this.numOfDiscsInColumn[col]-1;
		 board[firstEmptyCellRow][col]=currentplayer;
		 this.numOfDiscsInColumn[col]++;
	 }
	 
	 /**
	  * Check if one of the players gets N checkers in a row (horizontally, vertically or diagonally) 
	  *  @return the value of winner. If winner=-1, nobody win and game continues; If winner=0/TIE, it's a tie;
	  * 			If winner=1, player1 wins; If winner=2, player2 wins. 
	  */
	 
	 public int isConnectN(){
		int tmp_winner=checkHorizontally();
		
		if(tmp_winner!=this.NOCONNECTION)
			return tmp_winner;
		
		 tmp_winner=checkVertically();
		 if(tmp_winner!=this.NOCONNECTION)
				return tmp_winner;
		 
		 tmp_winner=checkDiagonally1();
		 if(tmp_winner!=this.NOCONNECTION)
				return tmp_winner; 
		 tmp_winner=checkDiagonally2();
		 if(tmp_winner!=this.NOCONNECTION)
				return tmp_winner; 
		 
		 return this.NOCONNECTION;
		 
	 }
	 
  public int checkHorizontally(){
	  int max1=0;
		 int max2=0;
		 boolean player1_win=false;
		 boolean player2_win=false;
		 //check each row, horizontally
		 for(int i=0;i<this.height;i++){
			 max1=0;
			 max2=0;
			for(int j=0;j<this.width;j++){
				if(board[i][j]==PLAYER1){
					max1++;
					max2=0;
					if(max1==N)
						 player1_win=true;
				}
				else if(board[i][j]==PLAYER2){
					max1=0;
					max2++;
					if(max2==N)
						 player2_win=true;
				}
				else{
					max1=0;
					max2=0;
				}
			}
		 } 
		 if (player1_win && player2_win)
			 return this.TIE;
		 if (player1_win)
			 return this.PLAYER1;
		 if (player2_win)
			 return this.PLAYER2;
		 
		 return this.NOCONNECTION;
  }

  public int checkVertically(){
	  //check each column, vertically
	  int max1=0;
	  int max2=0;
	  boolean player1_win=false;
	  boolean player2_win=false;
		 
		 for(int j=0;j<this.width;j++){
			 max1=0;
			 max2=0;
			for(int i=0;i<this.height;i++){
				if(board[i][j]==PLAYER1){
					max1++;
					max2=0;
					if(max1==N)
						 player1_win=true;
				}
				else if(board[i][j]==PLAYER2){
					max1=0;
					max2++;
					if(max2==N)
						player2_win=true;
				}
				else{
					max1=0;
					max2=0;
				}
			}
		 } 
		 if (player1_win && player2_win)
			 return this.TIE;
		 if (player1_win)
			 return this.PLAYER1;
		 if (player2_win)
			 return this.PLAYER2;
		 
		 return this.NOCONNECTION;
  }
  
   public int checkDiagonally1(){
	 //check diagonally y=-x+k
	   int max1=0;
	   int max2=0;
	   boolean player1_win=false;
	   boolean player2_win=false;
	   int upper_bound=height-1+width-1-(N-1);
	   
		 for(int k=N-1;k<=upper_bound;k++){			
			 max1=0;
			 max2=0;
			 int x,y;
			 if(k<width) 
				 x=k;
			 else
				 x=width-1;
			 y=-x+k;
			 
			while(x>=0  && y<height){
				// System.out.println("k: "+k+", x: "+x+", y: "+y);
				if(board[height-1-y][x]==PLAYER1){
					max1++;
					max2=0;
					if(max1==N)
						 player1_win=true;
				}
				else if(board[height-1-y][x]==PLAYER2){
					max1=0;
					max2++;
					if(max2==N)
						player2_win=true;
				}
				else{
					max1=0;
					max2=0;
				}
				x--;
				y++;
			}	 
			 
		 }
		 if (player1_win && player2_win)
			 return this.TIE;
		 if (player1_win)
			 return this.PLAYER1;
		 if (player2_win)
			 return this.PLAYER2;
		 
		 return this.NOCONNECTION;
   }
	 
   public int checkDiagonally2(){
	 //check diagonally y=x-k
	   int max1=0;
	   int max2=0;
	   boolean player1_win=false;
	   boolean player2_win=false;
	   int upper_bound=width-1-(N-1);
	   int  lower_bound=-(height-1-(N-1));
	  // System.out.println("lower: "+lower_bound+", upper_bound: "+upper_bound);
		 for(int k=lower_bound;k<=upper_bound;k++){			
			 max1=0;
			 max2=0;
			 int x,y;
			 if(k>=0) 
				 x=k;
			 else
				 x=0;
			 y=x-k;
			while(x>=0 && x<width && y<height){
				// System.out.println("k: "+k+", x: "+x+", y: "+y);
				if(board[height-1-y][x]==PLAYER1){
					max1++;
					max2=0;
					if(max1==N)
						 player1_win=true;
				}
				else if(board[height-1-y][x]==PLAYER2){
					max1=0;
					max2++;
					if(max2==N)
						player2_win=true;
				}
				else{
					max1=0;
					max2=0;
				}
				x++;
				y++;
			}	 
			 
		 }	 //end for y=x-k
		 
		 if (player1_win && player2_win)
			 return this.TIE;
		 if (player1_win)
			 return this.PLAYER1;
		 if (player2_win)
			 return this.PLAYER2;
		 
		 return this.NOCONNECTION;
   }

	public void makeHeuristic()
	{
		if (isConnectN() == 1)
			this.heuristic = 2147483647; // max value for a long
		else if (isConnectN() == 2)
			this.heuristic = -2147483648; // min value for long
		else
		{
			this.heuristic = 0;
			for(int i=N-1; i>0; i--)
			{
				this.heuristic = heuristic + (1<<i-1 * countNInARow(i,1)) - (1<<i-1 * countNInARow(i,2));
			}
		}
	}

	public int countNInARow(int n, int player)
   	{
		return countHorizontally(n,player) + countVertically(n,player) + countDiagonally1(n,player) + countDiagonally2(n,player);
	}

	public int countHorizontally(int n,int player)
	{
	// this method counts the number of times a specific player has "n" tokens
	// in a row with nothing blocking the player from adding another colinear token
		int inARow = 0; // tracks the number of pieces found in a row at any given time
		int totalCount = 0; // tracks the number of "n" tokens in a row with nothing blocking the player from adding another colinear token found
		for(int i=0;i<this.height;i++) // itterates through all the rows
		{
			inARow = 0;
			for(int j=0;j<this.width;j++) // iterates through each space in a row
			{
				if(board[i][j] == player) // if the piece in a space belongs to the given player
				{
					inARow++;
					if(inARow == n) // if we have found an instance of "n" tokens in a row
					{
						if ((j + 1 < width) && (j - n > 0) && (board[i][j + 1] != emptyCell) && (board[i][j - n] != emptyCell)) // check if the player cannot add a colinear piece
						{
							inARow = 1; // reset the count of InARow if we cannot add a piece
						}
						else if ((j + 1 < width) && (board[i][j + 1] == emptyCell)) // if we have found an opportunity to expand colinearly in one direction
						{
							totalCount++; //  add to the total count
							inARow = 1;
						}
						else if ((j - n > 0) && board[i][j - n] == emptyCell)  // if we have found an opportunity to expand colinearly in the other direction
						{
							totalCount++;
							inARow = 1;
						}
					}
				}
				else
				{
					inARow = 0; // if the space doen't have a piece belinging to the given player then reset the count of InARow
				}
			}
		}
		return totalCount;
	}

	public int countVertically(int n,int player)
	{
	// this method counts the number of times a specific player has "n" tokens
	// in a row with nothing blocking the player from adding another colinear token
		int inARow = 0; // tracks the number of pieces found in a row at any given time
		int totalCount = 0; // tracks the number of "n" tokens in a row with nothing blocking the player from adding another colinear token found
		for(int j=0;j<this.width;j++) // itterates through all the columns
		{
			inARow = 0;
			for(int i=0;i<this.height;i++) // iterates through each space in a column
			{
				if(board[i][j] == player) // if the piece in a space belongs to the given player
				{
					inARow++;
					if(inARow == n) // if we have found an instance of "n" tokens in a row
					{
						if ((i + 1 < width) && (i - n > 0) && (board[i + 1][j] != emptyCell) && (board[i - n][j] != emptyCell)) // check if the player cannot add a colinear piece
						{
							inARow = 1; // reset the count of InARow if we cannot add a piece
						}
						else if ((i + 1 < width) && (board[i + 1][j] == emptyCell)) // if we have found an opportunity to expand colinearly in one direction
						{
							totalCount++; //  add to the total count
							inARow = 1;
						}
						else if ((i - n > 0) && board[i - n][j] == emptyCell)  // if we have found an opportunity to expand colinearly in the other direction
						{
							totalCount++;
							inARow = 1;
						}
						
					}
				}
				else
				{
					inARow = 0; // if the space doen't have a piece belinging to the given player then reset the count of InARow
				}
			}
		}
		return totalCount;
	}
 
  	public int countDiagonally1(int n,int player)
  	{
		int inARow = 0; // tracks the number of pieces found in a row at any given time
		int totalCount = 0; // tracks the number of "n" tokens in a row with nothing blocking the player from adding another colinear token found
		int upper_bound=height-1+width-1-(N-1);
		for(int k=N-1;k<=upper_bound;k++)
		{			
			inARow = 0;
			int x,y;
			if(k < width) 
				x = k;
			else
				x = width - 1;
			y = -x + k; 
			while(x >= 0 && y < height)
			{
				if(board[height - 1 - y][x] == player)
				{
					inARow++;
					if(inARow == n)
					{
						if ((height - y < height) && (x - 1 > 0) && (height - 1 - y - n > 0) && (x + n < width) && (board[height - y][x - 1] != emptyCell) && (board[height - 1 - y - n][x + n] != emptyCell)) // check if the player cannot add a colinear piece
						{
							inARow = 1; // reset the count of InARow if we cannot add a piece
						}
						else if ((height - y < height) && (x - 1 > 0) && (board[height - y][x - 1] == emptyCell)) // if we have found an opportunity to expand colinearly in one direction
						{
							totalCount++; //  add to the total count
							inARow = 1;
						}
						else if ((height - 1 - y - n > 0) && (x + n < width) && (board[height - 1 - y - n][x + n] == emptyCell))  // if we have found an opportunity to expand colinearly in the other direction
						{
							totalCount++;
							inARow = 1;
						}
					}
				}
				else
				{
					inARow = 0;
				}
				x--;
				y++;
			}	 
		}
		return totalCount;
	}

	public int countDiagonally2(int n,int player)
  	{
		int inARow = 0; // tracks the number of pieces found in a row at any given time
		int totalCount = 0; // tracks the number of "n" tokens in a row with nothing blocking the player from adding another colinear token found
		int upper_bound=width-1-(N-1);
		int lower_bound=-(height-1-(N-1));
		for(int k=lower_bound;k<=upper_bound;k++)
		{			
			inARow = 0;
			int x,y;
			if(k>=0) 
				x = k;
			else
				x = 0;
			y= x - k;
			while(x>=0 && x<width && y<height)
			{
				if(board[height - 1 - y][x] == player)
				{
					inARow++;
					if(inARow == n)
					{
						if ((height - y < height) && (x + 1 > 0) && (height - 1 - y - n > 0) && (x - n < width) && (board[height - y][x + 1] != emptyCell) && (board[height - 1 - y - n][x - n] != emptyCell)) // check if the player cannot add a colinear piece
						{
							inARow = 1; // reset the count of InARow if we cannot add a piece
						}
						else if ((height - y < height) && (x + 1 > 0) && (board[height - y][x + 1] == emptyCell)) // if we have found an opportunity to expand colinearly in one direction
						{
							totalCount++; //  add to the total count
							inARow = 1;
						}
						else if ((height - 1 - y - n > 0) && (x - n < width) && (board[height - 1 - y - n][x - n] == emptyCell))  // if we have found an opportunity to expand colinearly in the other direction
						{
							totalCount++;
							inARow = 1;
						}
					}
				}
				else
				{
					inARow = 0;
				}
				x++;
				y++;
			}	 
		}
		return totalCount;
	}
   
	public boolean isFull(){
		for(int i=0;i<height;i++)
			for(int j=0;j<width;j++){
				if(board[i][j]==this.emptyCell)
					return false;
			}
		return true;
	}
	 
	 
	 public void setBoard(int row, int col, int player){
		 if(row>=height || col>=width)
			 throw new IllegalArgumentException("The row or column number is out of bound!");
		 if(player!=this.PLAYER1 && player!=this.PLAYER2)
			 throw new IllegalArgumentException("Wrong player!");
		 this.board[row][col]=player;
	 }
	 
	 /**
	  * test is connect N diagonally y=-x+k
	  * */ 
	 private void test1(){
		 dropADiscFromTop(2,1);
		 dropADiscFromTop(1,2);
		 dropADiscFromTop(1,1);
		 dropADiscFromTop(0,2);
		 dropADiscFromTop(0,1);
		 dropADiscFromTop(2,2);
		 dropADiscFromTop(0,1);
		 printBoard();
		 int tmp_winner= checkDiagonally1();
		 System.out.println("Winner: "+tmp_winner);	
	 }
	 /**
	  * test is connect N diagonally y=-x+k
	  * */ 
	 private void test2(){		
		 setBoard(1,2,this.PLAYER1);
		 setBoard(2,3,this.PLAYER1);
		 setBoard(3,4,this.PLAYER1);		 
		 printBoard();
		 int tmp_winner= checkDiagonally1();
		 //int tmp_winner= isConnectN();
		 System.out.println("Winner: "+tmp_winner);	
	 }

	 /**
	  * test is connect N diagonally y=x-k
	  * */ 
	 private void test3(){		
//		 setBoard(2,5,this.PLAYER2);
//		 setBoard(4,3,this.PLAYER2);
//		 setBoard(3,4,this.PLAYER2);
		 setBoard(5,4,this.PLAYER1);
		 setBoard(4,5,this.PLAYER1);
		 setBoard(3,6,this.PLAYER1);
		 printBoard();
		 int tmp_winner= checkDiagonally2();
		 //int tmp_winner= isConnectN();
		 System.out.println("Winner: "+tmp_winner);	
	 }
	 
	 
	 /**
	  * test is connect N diagonally y=-x+k
	  * */ 
	 private void test4(){
		 setBoard(2,0,this.PLAYER1);
		 setBoard(3,1,this.PLAYER1);
		// setBoard(4,2,this.PLAYER1);
		 setBoard(5,3,this.PLAYER1);		 
		 printBoard();
		 int tmp_winner= checkDiagonally1();
		 //int tmp_winner= isConnectN();
		 System.out.println("Winner: "+tmp_winner);	
	 }
	 /**
	  * test should ends with tie
	  * */ 
	 private void test5(){
		 setBoard(2,0,this.PLAYER1);
		 setBoard(3,1,this.PLAYER1);
		 setBoard(4,2,this.PLAYER1);
		// setBoard(1,4,this.PLAYER1);
		 
//		 setBoard(3,1,this.PLAYER1);
//		 setBoard(3,2,this.PLAYER1);
//		 setBoard(3,3,this.PLAYER1);
//		 setBoard(3,4,this.PLAYER1);
		 
		 setBoard(0,3,this.PLAYER2);
		 setBoard(2,5,this.PLAYER2);
		 setBoard(2,3,this.PLAYER2);
		 setBoard(1,4,this.PLAYER2);
		 printBoard();
		// int tmp_winner= this.checkHorizontally();
		 int tmp_winner= this.checkDiagonally1();
		 System.out.println("Winner: "+tmp_winner);	
	 } 
	 
	 public static void main(String [] arg){
		 Board b=new Board(6,7,3);

 		 b.printBoard();
//		 b.test1();
//		 b.test2();
//       b.test3();
 //        b.test5();
	 }
}
