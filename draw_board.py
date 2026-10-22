import pygame

from constants import *


def draw_squares(screen):
    for row in range(0,8):
        for col in range(0, 8):
            y = row * SQUARE_SIZE
            x = col * SQUARE_SIZE
            if (row + col) % 2 == 0:
                color = WHITE_SQUARE
            else:
                color = BLACK_SQUARE
            pygame.draw.rect(screen,color,(x, y, SQUARE_SIZE, SQUARE_SIZE))
