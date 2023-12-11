import pygame
from board import Board
from dragger import Dragger

from const import *

class Render:

    def __init__(self):
        self.font = pygame.font.Font(None, 100)
        self.menu_font = pygame.font.SysFont("comicsans", 80)
        # Colors
        self.light_green = (234, 235, 200)
        self.dark_green = (119, 154, 88)
        self.move_color = '#C86464'
        self.pass_color = '#FFFF00'

    #show methods
    def show_menu(self, screen):
        screen.fill((128,128,128))
        font = pygame.font.SysFont("comicsans", 80)
        title = font.render("Online Razzle Dazzle", 1, (0,128,0))
        screen.blit(title, (WIDTH/2-title.get_width()/2,400))
        pygame.display.update()


    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col) % 2 == 0:
                    color = self.light_green
                else:
                    color = self.dark_green
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    
    def show_pieces(self, surface, game):
         for row in range(ROWS):
            for col in range(COLUMNS):
                # is there a piece?
                    if game.board.squares[row][col].has_piece():
                        piece = game.board.squares[row][col].piece
                        # blits all the pieces that is not the dragged piece
                        if piece is not self.dragger.piece:
                            img = pygame.image.load(piece.texture)
                            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                            piece.texture_rect = img.get_rect(center=img_center)
                            surface.blit(img, piece.texture_rect)

    def show_moves(self, surface, game):
        if game.dragger.dragging:
            piece = game.dragger.piece
            # loop through valid moves
            for move in piece.moves:
                #color
                color = self.move_color if (move.final.row + move.final.col) % 2 == 0 else self.move_color
                # rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                #blit
                pygame.draw.rect(surface, color, rect)

    def show_passes(self, surface, game):
        if game.dragger.dragging:
            ball = game.dragger.ball
            # loop through valid moves
            for a_pass in ball.passes:
                #color
                color = self.pass_color if (a_pass.final.row + a_pass.final.col) % 2 == 0 else self.pass_color
                # rect
                rect = (a_pass.final.col * SQSIZE, a_pass.final.row * SQSIZE, SQSIZE, SQSIZE)
                #blit
                pygame.draw.rect(surface, color, rect)


    def show_ball(self, surface, game):
        for row in range(ROWS):
            for col in range(COLUMNS):
            # is there a ball?
                if game.board.squares[row][col].has_piece():
                    piece = game.board.squares[row][col].piece
                    if piece.has_ball():
                        if piece.ball is not game.dragger.ball:
                            img = pygame.image.load(piece.ball.texture)
                            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                            piece.ball.texture_rect = img.get_rect(center=img_center)
                            surface.blit(img, piece.ball.texture_rect)
    
    def show_win(self, surface, color, did_win, game):
        if did_win == True:
            msg= self.font.render(color+ " Wins!", True, '#000000')
            rect = (200, 400,400, 100)
            pygame.draw.rect(surface, '#FFFFFF', rect)
            surface.blit(msg, (200,420))
