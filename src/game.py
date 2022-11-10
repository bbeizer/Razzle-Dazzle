import pygame
from board import Board
from dragger import Dragger


from const import *

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    #show methods
    def show_bg(self, surface):

        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col) % 2 == 0:
                    color = (234,235,200) # light green
                else:
                    color = (119,154, 88) # dark green
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    
    def show_pieces(self, surface):
         for row in range(ROWS):
            for col in range(COLUMNS):
                # is there a piece?
                    if self.board.squares[row][col].has_piece():
                        piece = self.board.squares[row][col].piece
                        # blits all the pieces that is not the dragged piece
                        if piece is not self.dragger.piece:
                            img = pygame.image.load(piece.texture)
                            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                            piece.texture_rect = img.get_rect(center=img_center)
                            surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            # loop through valid moves
            for move in piece.moves:
                #color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C86464'
                # rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                #blit
                pygame.draw.rect(surface, color, rect)

    def show_passes(self, surface):
        if self.dragger.dragging:
            ball = self.dragger.ball
            # loop through valid moves
            for a_pass in ball.passes:
                #color
                color = '#FFFF00' if (a_pass.final.row + a_pass.final.col) % 2 == 0 else '#FFFF00'
                # rect
                rect = (a_pass.final.col * SQSIZE, a_pass.final.row * SQSIZE, SQSIZE, SQSIZE)
                #blit
                pygame.draw.rect(surface, color, rect)


    def show_ball(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
            # is there a ball?
                    if self.board.squares[row][col].has_piece():
                        piece = self.board.squares[row][col].piece
                        if piece.has_ball() == True:
                            ball = piece.ball
                            img = pygame.image.load(ball.texture)
                            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                            piece.texture_rect = img.get_rect(center=img_center)
                            surface.blit(img, piece.texture_rect)

    