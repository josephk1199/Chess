import pygame

from constants import *



def draw_squares(screen):
    for row in range(0,8):
        for col in range(0, 8):
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
            piece_images[name] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
    return piece_images

def draw_pieces(screen, piece_images, layout):
    for square, piece in layout.items():
        if piece is None:
            continue
        file_id = FILES.index(square[0])
        rank_id = BOARD_SIZE - int(square[1])
        x = file_id * SQUARE_SIZE
        y = rank_id * SQUARE_SIZE
        name = f"{piece.color}_{piece.kind}"
        image = piece_images[name]
        screen.blit(image, (x, y))
