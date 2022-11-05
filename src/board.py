from const import *
from square import Square

class Board:

    # Spot[][] board;
  
    def __init__(self):
        self.squares = []

    def _create(self):
        
        square = self.square

        #creating an empty board
        self.squares = [[0,0,0,0,0,0,0,0,0] for col in range(COLUMNS)]
        
        for row in range(ROWS):
            for col in range (COLUMNS):
                square[row][col] = Square(row,col)




    def _add_piece(self):
        pass
#     public Board(){	
#     	this.board = new Spot[8][8];
#         this.resetBoard();
#     }
  
#     public Spot getBox(int x, int y) throws Exception {
  
#         if (x < 0 || x > 7 || y < 0 || y > 7) {
#             throw new Exception("Index out of bound");
#         }
  
#         return board[x][y];
#     }
  
#     public void resetBoard(){
    	
#         // initialize white pieces
#         board[0][0] = new Spot(0, 0, null);
#         board[0][1] = new Spot(0, 1, null);
#         board[0][2] = new Spot(0, 2, new Knight(true, null));
#         board[0][3] = new Spot(0, 3, new Knight(true, new Ball()));
#         board[0][4] = new Spot(0, 4, new Knight(true, null));
#         board[0][5] = new Spot(0, 5, new Knight(true, null));
#         board[0][6] = new Spot(0, 6, null);
#         board[0][7] = new Spot(0, 7, null);
        
#         // initialize remaining boxes without any piece
#         for (int i = 1; i < 7; i++) {
#             for (int j = 0; j < 8; j++) {
#                 board[i][j] = new Spot(i, j, null);
#             }
#         }
        
#         // initialize black pieces
#         board[0][0] = new Spot(7, 0, null);
#         board[0][1] = new Spot(7, 1, null);
#         board[0][2] = new Spot(7, 2, new Knight(true, null));
#         board[0][3] = new Spot(7, 3, new Knight(true, null));
#         board[0][4] = new Spot(7, 4, new Knight(true, new Ball()));
#         board[0][5] = new Spot(7, 5, new Knight(true, null));
#         board[0][6] = new Spot(7, 6, null);
#         board[0][7] = new Spot(7, 7, null);
        
#     }
    
    
# }