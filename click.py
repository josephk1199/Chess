from coords import *


def click_handling(pos, layout, selected, player_turn, moves):
    clicked = pixels_to_square(pos)
    piece = layout[clicked]
    if clicked == selected:
        selected = None
        moves = []
    elif piece is not None and piece.color == player_turn:
        selected = clicked
        moves = piece.get_moves(clicked, layout)
    elif selected is not None and clicked in moves:
        layout[clicked] = layout[selected]
        layout[selected] = None
        selected = None
        moves = []
        if player_turn == "white":
            player_turn = "black"
        else:
            player_turn = "white"
    return selected, player_turn, moves
