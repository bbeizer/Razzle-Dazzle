import os
pieces = []
class Piece:
	def __init__(self, name, color, current_square, ball=None, texture=None, texture_rect=None):
		self.name = name
		self.color = color
		self.ball = ball
		self.initial_square = current_square
		self.current_square = self.initial_square
		self.texture = texture
		self.moves = []
		self.moved = False
		self.set_texture()
		self.texture_rect = texture_rect
		pieces.append(self)

	def set_texture(self, size=80):
		self.texture = os.path.join(f'assets/images/img-{size}px/{self.color}_piece.png')
    
	def add_move(self, move):
		self.moves.append(move)

	def clear_moves(self):
		self.moves = []

	def clear_passes(self):
		self.passes = []

	def has_ball(self):
		return self.ball != None

	@staticmethod
	def set_initial_squares():
		for piece in pieces:
			piece.initial_square = piece.current_square
			piece.moved = False

class Knight(Piece):

	def __init__(self, color, current_square, ball):
		super().__init__('Knight', color, current_square, ball)

class Bishop(Piece):

	def __init__(self, color):
		super().__init__('Bishop', color)

class Rook(Piece):

	def __init__(self, color):
		super().__init__('Rook', color)

class Queen(Piece):

	def __init__(self, color, ball):
		super().__init__('Queen', color)


	