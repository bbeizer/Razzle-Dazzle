import os

class Piece:

	def __init__(self, name, color, ball=None, texture=None, texture_rect=None):
		self.name = name
		self.color = color
		self.ball = ball
		self.texture = texture
		self.moves = []
		self.moved = False
		self.set_texture()
		self.texture_rect = texture_rect


	def set_texture(self, size=80):
		self.texture = os.path.join(f'assets/images/img-{size}px/{self.color}_piece.png')

		pass


class Knight(Piece):
	
	def __init__(self, color):
		super().__init__('Knight', color)

class Bishop(Piece):

	def __init__(self, color):
		super().__init__('Bishop', color)

class Rook(Piece):

	def __init__(self, color):
		super().__init__('Rook', color)

class Queen(Piece):

	def __init__(self, color, ball):
		super().__init__('Queen', color)


	