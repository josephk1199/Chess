
# Pawn attack not included yet...
from pieces import King


def is_attacked(square, by_color, layout):
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
    pass
