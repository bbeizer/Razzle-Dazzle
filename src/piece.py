import os

class Piece:

	def __init__(self, name, color, ball=None, texture=None, texture_rect=None):
		self.name = name
		self.color = color
		self.ball = ball
		self.texture = texture
		self.moves = []
		self.moved = False
		self.passes = []
		self.passed = False
		self.set_texture()
		self.texture_rect = texture_rect


	def set_texture(self, size=80):
		self.texture = os.path.join(f'assets/images/img-{size}px/{self.color}_piece.png')
    
	def add_move(self, move):
		self.moves.append(move)

	def add_pass(self, a_pass):
		self.passes.append(a_pass)

	def clear_moves(self):
		self.moves = []

	def clear_passes(self):
		self.passes = []

	def has_ball(self):
		return self.ball != None





class Knight(Piece):
	
	def __init__(self, color, ball):
		super().__init__('Knight', color, ball)

class Bishop(Piece):

	def __init__(self, color):
		super().__init__('Bishop', color)

class Rook(Piece):

	def __init__(self, color):
		super().__init__('Rook', color)

class Queen(Piece):

	def __init__(self, color, ball):
		super().__init__('Queen', color)


	