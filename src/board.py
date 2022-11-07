from const import *
from square import Square
from ball import Ball
from piece import *

class Board:
  
    def __init__(self):
        self.squares = []
        self.squares = [[0,0,0,0,0,0,0,0,0] for col in range(COLUMNS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):  
        for row in range(ROWS):
            for col in range (COLUMNS):
                self.squares[row][col] = Square(row,col)




    def _add_pieces(self, color):
        if color == 'white':
            self.squares[7][2] = Square(7, 2, Knight(color))
            self.squares[7][3] = Square(7, 3, Knight(color))
            self.squares[7][4] = Square(7, 4, Knight(color))
            self.squares[7][5] = Square(7, 5, Knight(color))
        else:
            self.squares[0][2] = Square(7, 2, Knight(color))
            self.squares[0][3] = Square(7, 3, Knight(color))
            self.squares[0][4] = Square(7, 4, Knight(color))
            self.squares[0][5] = Square(7, 5, Knight(color))



    
        
