import pygame
from const import *


class Dragger:
    
    def __init__(self):
        self.piece = None
        self.ball = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
    
    # blit methods 
    def update_blit(self, surface):
        #texture
        # for piece
        if self.piece != None:
            self.piece.set_texture(size=80)
            #img
            img = pygame.image.load(self.piece.texture)
            #rect
            img_center = (self.mouseX, self.mouseY)
            self.piece.texture_rect = img.get_rect(center=img_center)
            surface.blit(img, self.piece.texture_rect)
        # for ball 
        else:
            self.ball.set_texture(size=80)
            #img
            img = pygame.image.load(self.ball.texture)
            #rect
            img_center = (self.mouseX, self.mouseY)
            self.ball.texture_rect = img.get_rect(center=img_center)
            surface.blit(img, self.ball.texture_rect) 

    
    #other methods
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False

    def drag_ball(self, ball):
        self.ball = ball
        self.dragging = True

    def undrag_ball(self):
        self.ball = None
        self.dragging = False


