
class Piece:

	def __init__(self, name, color, ball=None, texture=None, texture_rect=None):
		self.name = name
		self.color = color
		self.texture = texture
		self.ball = ball
		self.set_texture()
		self.texture_rect = texture_rect


	def set_texture():
		# create a texture piece later for all the pieces that arially looks like it has a hole in it 
		# and maybe put a dot inside the circle and set the texture of all the pieces to this
		
		pass



class Knight(Piece):
	
	def __init__(self, color):
		super.__init__('Knight', color)

class Bishop(Piece):

	def __init__(self, color):
		super().__init__('Bishop', color)

class Rook(Piece):

	def __init__(self, color):
		super().__init__('Rook', color)

class Queen(Piece):

	def __init__(self, color):
		super().__init__('Queen', color)


	
# 	private boolean isWhite = false;
# 	private Ball ball = null;
	
# 	public Piece(boolean white, Ball ball) {
# 		this.setWhite(white);
# 		this.setBall(ball);
# 	}
	
# 	public boolean isWhite() {
# 		return this.isWhite
# 				;
# 	}
	
# 	public void setWhite(boolean white) {
# 		this.isWhite = white;
# 	}
	
# 	public Ball hasBall() {
# 		return this.ball;
# 	}
	
# 	public void setBall(Ball ball) {
# 		this.ball = ball;
# 	}
	
	
# 	//public boolean canPassBall() {
# 	//	
# 	//}
	
# 	public boolean canMoveBall(Board board, Spot start, Spot end) {
# 		return false;
# 	}
# 	public abstract boolean canMove(Board board, Spot start, Spot end);
	
# }