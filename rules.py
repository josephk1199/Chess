from coords import file_rank_to_square, square_to_file_rank


def is_attacked(square, by_color, layout): # Pawn attack not included yet...
    for a_square, piece in layout.items():
        if piece is None:
            continue
        if piece.color != by_color:
            continue
        if square in piece.get_attacks(a_square, layout):
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
    elif moving_piece.kind == "king":
        candidates = moving_piece.get_moves(square, layout) + castling(square, layout)
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

def has_moves(color, layout, en_passant_square = None):
    for a_square, piece in layout.items():
        if piece is None:
            continue
        if piece.color != color:
            continue
        if legal_moves(a_square, layout, en_passant_square):
            return True
    return False

def game_status(color, layout, en_passant_square = None):
    if color == "white":
        enemy = "black"
    else:
        enemy = "white"
    if has_moves(color, layout, en_passant_square):
        return "playing"
    elif is_attacked(find_king(color, layout), enemy, layout):
        return "checkmate"
    else:
        return "stalemate"

def castling(square, layout):
    king = layout[square]
    if king.color == "white":
        back_rank = 1
        enemy = "black"
    else:
        back_rank = 8
        enemy = "white"
    if king.has_moved:
        return []
    if is_attacked(square, enemy, layout):
        return []
    #Kingside Castling
    result = []
    rook_square = "h" + str(back_rank)
    rook = layout[rook_square]
    if rook is not None and rook.kind == "rook" and not rook.has_moved and rook.color == king.color:
        f_square = "f" + str(back_rank)
        g_square = "g" + str(back_rank)
        if layout[f_square] is None and not is_attacked(f_square, enemy, layout) and layout[g_square] is None and not is_attacked(g_square, enemy, layout) :
            result.append(g_square)
    #Queenside Castling
    rook_square = "a" + str(back_rank)
    rook = layout[rook_square]
    if rook is not None and rook.kind == "rook" and not rook.has_moved and rook.color == king.color:
        b_square = "b" + str(back_rank)
        c_square = "c" + str(back_rank)
        d_square = "d" + str(back_rank)
        if layout[b_square] is None and layout[c_square] is None and not is_attacked(c_square, enemy, layout) and layout[d_square] is None and not is_attacked(d_square, enemy, layout):
            result.append(c_square)
    return result
