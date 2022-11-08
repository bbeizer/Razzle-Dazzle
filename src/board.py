import pygame
from const import *
from move import Move
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
            self.squares[7][2] = Square(7, 2, Knight(color, None))
            self.squares[7][3] = Square(7, 3, Knight(color, Ball()))
            self.squares[7][4] = Square(7, 4, Knight(color, None))
            self.squares[7][5] = Square(7, 5, Knight(color, None))
        else:
            self.squares[0][2] = Square(7, 2, Knight(color, None))
            self.squares[0][3] = Square(7, 3, Knight(color, None))
            self.squares[0][4] = Square(7, 4, Knight(color, Ball()))
            self.squares[0][5] = Square(7, 5, Knight(color, None))

    def calc_moves(self, piece, row, col, bool=True):
        '''
            Calculate all the possible (valid) moves of pieces with Knight/Rook/Bishop/Queen type movement
        '''
        def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]
            for possible_move in possible_moves:
                
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty():
                        # create squares of new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) 
                        # creating move
                        move = Move(initial, final)
                        # append new valid move
                        piece.add_move(move)
        
        if isinstance(piece, Knight):
            knight_moves()
        
        elif isinstance(piece, Rook):
            pass

        elif isinstance(piece, Bishop):
            pass

        elif isinstance(piece, Bishop):
            pass



    
        
