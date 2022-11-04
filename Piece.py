
public abstract class Piece {
	
	private boolean isWhite = false;
	private Ball ball = null;
	
	public Piece(boolean white, Ball ball) {
		this.setWhite(white);
		this.setBall(ball);
	}
	
	public boolean isWhite() {
		return this.isWhite
				;
	}
	
	public void setWhite(boolean white) {
		this.isWhite = white;
	}
	
	public Ball hasBall() {
		return this.ball;
	}
	
	public void setBall(Ball ball) {
		this.ball = ball;
	}
	
	
	//public boolean canPassBall() {
	//	
	//}
	
	public boolean canMoveBall(Board board, Spot start, Spot end) {
		return false;
	}
	public abstract boolean canMove(Board board, Spot start, Spot end);
	
}