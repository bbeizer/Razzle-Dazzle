import pygame
import os

from sound import Sound


class Config:
    def __init__(self):
        self.move_sound = Sound(os.path.join("assets/sounds/move.wav"))
        self.pass_sound = Sound(os.path.join("assets/sounds/click.wav"))
