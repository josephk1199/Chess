import pygame
import pygame.gfxdraw

from constants import *
from coords import square_to_pixels
from pieces import Bishop, Knight, Queen, Rook


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

def draw_pieces(screen, piece_images, layout, flipped=False):
    for square, piece in layout.items():
        if piece is None:
            continue
        x, y = square_to_pixels(square, flipped)
        name = f"{piece.color}_{piece.kind}"
        image = piece_images[name]
        screen.blit(image, (x, y))

def highlight_selected(screen, selected, flipped=False):
    if selected is None:
        return
    x, y = square_to_pixels(selected,flipped)
    pygame.draw.rect(screen,HIGHLIGHTED_COLOR,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_dots(screen, moves, flipped=False):
    for move in moves:
        x, y = square_to_pixels(move, flipped)
        pygame.gfxdraw.filled_circle(screen, x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2, DOT_RADIUS, DOT_COLOR)
        pygame.gfxdraw.aacircle(screen, x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2, DOT_RADIUS, DOT_COLOR)

def draw_game_over(screen, font, status, player_turn, button):

    if status == "playing":
        return
    if status == "stalemate":
        words = font.render("Game Over - Stalemate", True, "black")
    else:
        if player_turn == "white":
            color = "black"
        else:
            color = "white"
        words = font.render(f"Checkmate {color.capitalize()} Wins!", True, "black")
    panel = pygame.Rect(0, 0, GAME_OVER_PANEL_SIZE, GAME_OVER_PANEL_SIZE)
    panel.center = (SCREEN_CENTER, SCREEN_CENTER)
    pygame.draw.rect(screen, GAME_OVER_PANEL_COLOR, panel)
    pygame.draw.rect(screen, NEW_GAME_BUTTON_COLOR, button)
    button_words = font.render("NEW GAME", True, "black")
    bw_spot = button_words.get_rect()
    bw_spot.center = button.center
    text_spot = words.get_rect()
    text_spot.center = panel.centerx, (panel.centery - 40)
    screen.blit(words, text_spot)
    screen.blit(button_words, bw_spot)

def make_promotion_buttons():
    promotion_buttons = {}
    start_x = SCREEN_CENTER - (SQUARE_SIZE * 2)
    for i, piece_class in enumerate([Queen, Rook, Bishop, Knight ]):
        promotion_buttons[piece_class] = pygame.Rect(start_x + i * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE)
        promotion_buttons[piece_class].centery = SCREEN_CENTER
    return promotion_buttons

def draw_promotion_menu(screen, piece_images, promotion_square, layout, promotion_buttons):
    if promotion_square is None:
        return
    promoting_color = layout[promotion_square].color

    for piece_class, rect in promotion_buttons.items():
        pygame.draw.rect(screen, PROMOTION_BOX_COLOR, rect)
        kind = piece_class(promoting_color).kind
        button_name = f"{promoting_color}_{kind}"
        screen.blit(piece_images[button_name], rect)
