
def is_attacked(square, by_color, layout): # Pawn attack not included yet...
    for a_square, piece in layout.items():
        if piece is None:
            continue
        if piece.color != by_color:
            continue
        if square in piece.get_moves(a_square, layout):
            return True
    return False

def find_king(color, layout):
    for a_square, piece in layout.items():
        if piece is None:
            continue
        if piece.color != color:
            continue
        if piece.kind == "king":
            return a_square
    return None

def legal_moves(square, layout):
    safe_moves = []
    moving_piece = layout[square]
    if moving_piece.color == "white":
        enemy = "black"
    else:
        enemy = "white"
    for target in moving_piece.get_moves(square, layout):
        captured = layout[target]
        layout[target] = moving_piece
        layout[square] = None
        in_check = is_attacked(find_king(moving_piece.color, layout), enemy, layout)
        layout[square] = moving_piece
        layout[target] = captured
        if not in_check:
            safe_moves.append(target)
    return safe_moves
