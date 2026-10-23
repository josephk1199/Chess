import pygame

from board import fill_board
from constants import *
from coords import pixels_to_square
from draw_board import draw_pieces, draw_squares, highlight_selected, load_images


def main():
    print(f"Starting Chess with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_SIZE}")
    print(f"Screen height: {SCREEN_SIZE}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    piece_images = load_images()
    layout = fill_board()
    clock = pygame.time.Clock()
    selected = None
    player_turn = "white"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = pixels_to_square(event.pos)
                piece = layout[clicked]
                if clicked == selected:
                    selected = None
                elif piece is not None and piece.color == player_turn:
                    selected = clicked
                elif selected is not None:
                    layout[clicked] = layout[selected]
                    layout[selected] = None
                    selected = None
                    if player_turn == "white":
                        player_turn = "black"
                    else:
                        player_turn = "white"
                print(selected)

        draw_squares(screen)
        highlight_selected(screen, selected)
        draw_pieces(screen, piece_images, layout)

        pygame.display.flip()
        clock.tick(60)




if __name__ == "__main__":
    main()
