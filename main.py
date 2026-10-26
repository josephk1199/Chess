import pygame

from board import fill_board
from click import click_handling
from constants import *
from draw_board import (
    draw_dots,
    draw_game_over,
    draw_pieces,
    draw_squares,
    highlight_selected,
    load_images,
)
from rules import game_status, has_moves


def main():
    print(f"Starting Chess with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_SIZE}")
    print(f"Screen height: {SCREEN_SIZE}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    piece_images = load_images()
    layout = fill_board()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    selected = None
    player_turn = "white"
    moves = []
    status = "playing"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and status == "playing":
                selected, player_turn, moves = click_handling(event.pos, layout, selected, player_turn, moves)
                status = game_status(player_turn, layout)
                print(moves)
                print(status)

        draw_squares(screen)
        highlight_selected(screen, selected)
        draw_pieces(screen, piece_images, layout)
        draw_dots(screen, moves)
        draw_game_over(screen, font, status, player_turn)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
