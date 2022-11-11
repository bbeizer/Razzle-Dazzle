import pygame
from a_pass import APass
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
            self.squares[7][2] = Square(7, 2, Knight(color, Square(7, 2), None))
            self.squares[7][3] = Square(7, 3, Knight(color, Square(7, 3), Ball()))
            self.squares[7][4] = Square(7, 4, Knight(color, Square(7, 4), None))
            self.squares[7][5] = Square(7, 5, Knight(color, Square(7, 5), None))
        else:
            self.squares[0][2] = Square(0, 2, Knight(color, Square(0,2), None))
            self.squares[0][3] = Square(0, 3, Knight(color, Square(0,3), None))
            self.squares[0][4] = Square(0, 4, Knight(color, Square(0,4), Ball()))
            self.squares[0][5] = Square(0, 5, Knight(color, Square(0,5), None))

    def move(self, piece, move):
        initial = move.initial
        final = move.final
        # console board move update
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece
        # move the piece
        piece.moved = True
        # clear valid moves for piece
        piece.clear_moves()

    def pass_ball(self, a_pass):
        initial = a_pass.initial
        final = a_pass.final
        # console board move update
        self.squares[initial.row][initial.col].piece.ball = None
        self.squares[final.row][final.col].piece.ball = Ball()
        # set last move
        self.last_pass = a_pass

        pass

    def valid_pass(self, ball, a_pass):
        return a_pass in ball.passes
    
    def valid_move(self, piece, move):
        return move in piece.moves

    def calc_passes(self, piece, row, col, bool=True):
        # every time this is called, the balls potential passes gets cleared
        ball = piece.ball
        ball.clear_passes()
        '''
            calculates all the possible valid passes a piece can make
        '''
        def straightline_passdirections(direction):
            for step in direction:
                row_incr, col_incr = step
                possible_pass_row = row 
                possible_pass_col = col
                for i in range(7):
                    possible_pass_row += row_incr
                    possible_pass_col += col_incr
                    if Square.in_range(possible_pass_row, possible_pass_col):
                        if self.squares[possible_pass_row][possible_pass_col].has_piece():
                            # if there is an opponent piece is blocking a pass, you move on to another potential pass
                            if self.squares[possible_pass_row][possible_pass_col].piece.color is not piece.color:
                                break
                            # add the pass to the the potential passes
                            else:
                                ball = piece.ball
                                initial = Square(row, col)
                                final  = Square(possible_pass_row, possible_pass_col)
                                a_pass = APass(initial, final)
                                ball.add_pass(a_pass)
                    else:
                        break

                            
                        
        # def blocked(row, col, piece_loc):
        #     print(row)
        #     print(col)
        #     print(piece_loc)
        #     return True
        #     # for incr in piece_loc:
        #     #     row_incr, col_incr = incr
        #     #     inbetween_row = row + row_incr
        #     #     inbetween_col = col + col_incr
        #     #     if self.squares[inbetween_row][inbetween_col].has_piece():
        #     #         return False
        #     # return True

        straightline_passdirections([
            (-1, 1), # up-right
            (-1, -1), # up-left
            (1, 1), # down-right
            (1, -1), # down-left
            (-1, 0), # up
            (0, 1), # right
            (1, 0), # down
            (0, -1) # left
        ])

  


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
        
        # takes pieces that move in a streight line and evaluates potential moves
        # will use this is I decide to allow user to change what kind of piece plays in 
        # the game
        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    # loops through possible squares
                    if Square.in_range(possible_move_row, possible_move_col):
                        # create squares of the possible new move
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        # create a possible new move
                        move = Move(initial, final)
                        piece.add_move(move)
                    elif self.squares[possible_move_row][possible_move_col].has_piece():
                        break
                    # not in range
                    else: 
                        break

        if isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Rook):
            straightline_moves([
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
            ])

        elif isinstance(piece, Bishop):
            straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
            ])

        elif isinstance(piece, Queen):
            straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1) # left
            ])




    
        
