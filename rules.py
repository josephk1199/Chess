from coords import square_to_file_rank, file_rank_to_square

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

def legal_moves(square, layout, en_passant_square=None):
    safe_moves = []
    moving_piece = layout[square]
    if moving_piece.color == "white":
        enemy = "black"
    else:
        enemy = "white"
    if moving_piece.kind == "pawn":
        candidates = moving_piece.get_moves(square, layout, en_passant_square)
    else:
        candidates = moving_piece.get_moves(square, layout)
    for target in candidates:
        captured = layout[target]
        is_en_passant = moving_piece.kind == "pawn" and target == en_passant_square
        passed_square = None
        passed_pawn = None
        if is_en_passant:
           file, _ = square_to_file_rank(target)
           _, rank = square_to_file_rank(square)
           passed_square = file_rank_to_square(file, rank)
           passed_pawn = layout[passed_square]
        layout[target] = moving_piece
        layout[square] = None
        if is_en_passant:
           layout[passed_square] = None
        in_check = is_attacked(find_king(moving_piece.color, layout), enemy, layout)
        layout[square] = moving_piece
        layout[target] = captured
        if is_en_passant:
          layout[passed_square] = passed_pawn
        if not in_check:
            safe_moves.append(target)
    return safe_moves

def has_moves(color, layout):
    for a_square, piece in layout.items():
        if piece is None:
            continue
        if piece.color != color:
            continue
        if legal_moves(a_square, layout):
            return True
    return False

def game_status(color, layout):
    if color == "white":
        enemy = "black"
    else:
        enemy = "white"
    if has_moves(color, layout):
        return "playing"
    elif is_attacked(find_king(color, layout), enemy, layout):
        return "checkmate"
    else:
        return "stalemate"
