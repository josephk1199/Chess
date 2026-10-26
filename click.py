from coords import *
from rules import legal_moves


def click_handling(pos, layout, selected, player_turn, moves, promotion_square, en_passant_square):
    clicked = pixels_to_square(pos)
    piece = layout[clicked]
    if clicked == selected:
        selected = None
        moves = []
    elif piece is not None and piece.color == player_turn:
        selected = clicked
        moves = legal_moves(clicked, layout, en_passant_square)
    elif selected is not None and clicked in moves:
        _, start_rank = square_to_file_rank(selected)
        layout[clicked] = layout[selected]
        layout[selected] = None
        layout[clicked].has_moved = True
        selected = None
        moves = []
        file, rank = square_to_file_rank(clicked)
        if layout[clicked].kind == "pawn" and clicked == en_passant_square:
            passed_square = file_rank_to_square(file, start_rank)
            layout[passed_square] = None
        if layout[clicked].kind == "pawn"  and abs(rank - start_rank) == 2:
            en_passant_square = file_rank_to_square(file, (start_rank + rank) // 2)
        else:
            en_passant_square = None
        if layout[clicked].kind == "pawn" and rank in [1, 8]:
            promotion_square = clicked
        else:
            if player_turn == "white":
                player_turn = "black"
            else:
                player_turn = "white"
    return selected, player_turn, moves, promotion_square, en_passant_square

def promotion_click(pos, layout, promotion_square, promotion_buttons, player_turn):
    for piece_class, rect in promotion_buttons.items():
        if rect.collidepoint(pos):
            piece_color = layout[promotion_square].color
            new_piece = piece_class(piece_color)
            layout[promotion_square] = new_piece
            promotion_square = None
            if player_turn == "white":
                player_turn = "black"
            else:
                player_turn = "white"
            break
    return promotion_square, player_turn
