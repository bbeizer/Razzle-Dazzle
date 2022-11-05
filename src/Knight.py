public class Knight extends Piece {

	public Knight(boolean white, Ball ball) {
		super(white, ball);
	}
	
    @Override
    public boolean canMove(Board board, Spot start, Spot end){
        // we can't move the piece to where another piece is
        if (end.getPiece() != null) {
            return false;
        }
  
        int x = Math.abs(start.getX() - end.getX());
        int y = Math.abs(start.getY() - end.getY());
        return x * y == 2;
    }

}