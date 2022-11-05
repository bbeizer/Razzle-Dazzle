import pygame

from const import *

class Game:

    def __init__(self):
        pass

    def show_bg(self, surface):
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col) % 2 == 0:
                    color = (234,235,200) # light green
                else:
                    color = (119,154, 88) # dark green

                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)




#     private Player[] players;
#     private Board board;
#     private Player currentTurn;
#     private GameStatus status;
#     private List<Move> movesPlayed;
  
#     private void initialize(Player p1, Player p2)
#     {
#         players[0] = p1;
#         players[1] = p2;
  
#         board.resetBoard();
  
#         if (p1.isWhiteSide()) {
#             this.currentTurn = p1;
#         }
#         else {
#             this.currentTurn = p2;
#         }
  
#         movesPlayed.clear();
#     }
  
#     public boolean isEnd()
#     {
#         return this.getStatus() != GameStatus.ACTIVE;
#     }
  
#     public boolean getStatus(){
    	
#         return this.status;
        
#     }
  
#     public void setStatus(GameStatus status){
    	
#         this.status = status;
#     }
  
#     public boolean playerMove(Player player, int startX, int startY, int endX, int endY){
    	
#         Spot startBox = board.getBox(startX, startY);
#         Spot endBox = board.getBox(startY, endY);
#         Move move = new Move(player, startBox, endBox);
#         return this.makeMove(move, player);
        
#     }
  
#     private boolean makeMove(Move move, Player player){
    	
#         Piece sourcePiece = move.getStart().getPiece();
#         if (sourcePiece == null) {
#             return false;
#         }
  
#         // valid player
#         if (player != currentTurn) {
#             return false;
#         }
  
#         if (sourcePiece.isWhite() != player.isWhiteSide()) {
#             return false;
#         }
  
#         // valid move?
#         if (!sourcePiece.canMove(board, move.getStart(), move.getEnd())) {
#             return false;
#         }
             
#         movesPlayed.add(move);
  
#         // move piece from the start box to end box
#         move.getEnd().setPiece(move.getStart().getPiece());
#         move.getStart.setPiece(null);
        
  
#         if (destPiece != null && destPiece instanceof King) {
#             if (player.isWhiteSide()) {
#                 this.setStatus(GameStatus.WHITE_WIN);
#             }
#             else {
#                 this.setStatus(GameStatus.BLACK_WIN);
#             }
#         }
  
#         // set the current turn to the other player
#         if (this.currentTurn == players[0]) {
#             this.currentTurn = players[1];
#         }
#         else {
#             this.currentTurn = players[0];
#         }
  
#         return true;
#     }
# }