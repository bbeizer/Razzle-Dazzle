
public class Bishop extends Piece {

	public Bishop(boolean white, Ball ball) {
		super(white, ball);
		// TODO Auto-generated constructor stub
	}

	@Override
	public boolean canMove(Board board, Spot start, Spot end) {
		
        int x = Math.abs(start.getX() - end.getX());
        int y = Math.abs(start.getY() - end.getY());
		
        return x==y;
	}

}
