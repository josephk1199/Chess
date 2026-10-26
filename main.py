import pygame

from board import new_game
from click import click_handling, promotion_click
from constants import *
from draw_board import (
    draw_dots,
    draw_game_over,
    draw_pieces,
    draw_promotion_menu,
    draw_squares,
    highlight_selected,
    load_images,
    make_promotion_buttons,
)
from rules import game_status


def main():
    print(f"Starting Chess with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_SIZE}")
    print(f"Screen height: {SCREEN_SIZE}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    piece_images = load_images()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    button = pygame.Rect(0,0,NEW_GAME_BUTTON_WIDTH, NEW_GAME_BUTTON_HEIGHT)
    button.center = SCREEN_CENTER, SCREEN_CENTER + 70
    promotion_buttons = make_promotion_buttons()
    layout, selected, player_turn, moves, status, promotion_square, en_passant_square = new_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and status == "playing" and promotion_square is None:
                selected, player_turn, moves, promotion_square, en_passant_square = click_handling(event.pos, layout, selected, player_turn, moves, promotion_square, en_passant_square)
                status = game_status(player_turn, layout)
                print(moves)
                print(status)
                print(promotion_square)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and promotion_square is not None:
                promotion_square, player_turn = promotion_click(event.pos, layout, promotion_square, promotion_buttons, player_turn)
                status = game_status(player_turn, layout)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and status != "playing" and button.collidepoint(event.pos) or event.type == pygame.KEYDOWN and event.key == pygame.K_r and event.mod & pygame.KMOD_META:
                layout, selected, player_turn, moves, status, promotion_square, en_passant_square = new_game()
                print("New Game")

        draw_squares(screen)
        highlight_selected(screen, selected)
        draw_pieces(screen, piece_images, layout)
        draw_dots(screen, moves)
        draw_game_over(screen, font, status, player_turn, button)
        draw_promotion_menu(screen, piece_images, promotion_square, layout, promotion_buttons)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
