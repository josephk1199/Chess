import pygame
import pygame.gfxdraw

from constants import *
from coords import square_to_pixels


def draw_squares(screen):
    for row in range(8):
        for col in range(8):
            y = row * SQUARE_SIZE
            x = col * SQUARE_SIZE
            if (row + col) % 2 == 0:
                color = LIGHT_SQUARE
            else:
                color = DARK_SQUARE
            pygame.draw.rect(screen,color,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def load_images():
    piece_images = {}
    for color in PIECE_COLORS:
        for kind in PIECES:
            name = f"{color}_{kind}"
            path = "assets/" + name + ".png"
            image = pygame.image.load(path).convert_alpha()
            piece_images[name] = pygame.transform.smoothscale(image, (SQUARE_SIZE, SQUARE_SIZE))
    return piece_images

def draw_pieces(screen, piece_images, layout):
    for square, piece in layout.items():
        if piece is None:
            continue
        x, y = square_to_pixels(square)
        name = f"{piece.color}_{piece.kind}"
        image = piece_images[name]
        screen.blit(image, (x, y))

def highlight_selected(screen, selected):
    if selected is None:
        return
    x, y = square_to_pixels(selected)
    pygame.draw.rect(screen,HIGHLIGHTED_COLOR,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_dots(screen, moves):
    for move in moves:
        x, y = square_to_pixels(move)
        pygame.gfxdraw.filled_circle(screen, x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2, DOT_RADIUS, DOT_COLOR)
        pygame.gfxdraw.aacircle(screen, x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2, DOT_RADIUS, DOT_COLOR)
