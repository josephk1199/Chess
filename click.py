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
        start_file, start_rank = square_to_file_rank(selected)
        layout[clicked] = layout[selected]
        layout[selected] = None
        layout[clicked].has_moved = True
        selected = None
        moves = []
        file, rank = square_to_file_rank(clicked)
        if layout[clicked].kind == "pawn" and clicked == en_passant_square:
            passed_square = file_rank_to_square(file, start_rank)
            layout[passed_square] = None
        if layout[clicked].kind == "king" and abs(file - start_file) == 2:
            if file > start_file:
                #Kingside
                rook_from = "h" + str(start_rank)
                rook_to = "f" + str(start_rank)
            else:
                #Queenside
                rook_from = "a" + str(start_rank)
                rook_to = "d" + str(start_rank)

            #Rook Move
            layout[rook_to] = layout[rook_from]
            layout[rook_from] = None
            layout[rook_to].has_moved = True

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
