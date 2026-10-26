from coords import *
from rules import legal_moves


def click_handling(pos, layout, selected, player_turn, moves, promotion_square):
    clicked = pixels_to_square(pos)
    piece = layout[clicked]
    if clicked == selected:
        selected = None
        moves = []
    elif piece is not None and piece.color == player_turn:
        selected = clicked
        moves = legal_moves(clicked, layout)
    elif selected is not None and clicked in moves:
        layout[clicked] = layout[selected]
        layout[selected] = None
        selected = None
        moves = []
        _, rank = square_to_file_rank(clicked)
        if layout[clicked].kind == "pawn" and rank in [1, 8]:
            promotion_square = clicked
        else:
            if player_turn == "white":
                player_turn = "black"
            else:
                player_turn = "white"
    return selected, player_turn, moves, promotion_square
