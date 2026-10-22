import pygame

from constants import *

class Piece:
    def __init__(self, color, kind) -> None:
        self.color = color
        self.kind = kind
