import pygame
from board import Board
from dragger import Dragger
from config import Config


from const import *

class Game:

    def __init__(self):
        self.current_player = 'White'
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()
        self.font = pygame.font.Font(None, 100)

    def play_sound(self, move):
        if move:
            self.config.move_sound.play()
        else:
            self.config.pass_sound.play()

    def next_turn(self):
        if self.current_player == 'White':
            self.current_player = 'Black'
        else:
            self.current_player = 'White'

    def reset(self):
        self.__init__()
