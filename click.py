from coords import *


def click_handling(pos, layout, selected, player_turn):
    clicked = pixels_to_square(pos)
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
    return selected, player_turn
