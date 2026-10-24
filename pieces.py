from coords import *


class Piece:
    def __init__(self, color, kind) -> None:
        self.color = color
        self.kind = kind

    def is_own_piece(self, square, layout) -> bool:
        piece = layout[square]
        return piece is not None and piece.color == self.color


class Pawn(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "pawn")



class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "knight")

    def get_moves(self, square, layout) -> list[str]:
        moveable_spaces: list[str] = []
        knights_moves = [
            (-1, +2),
            (+1, +2),
            (-2, +1),
            (+2, +1),
            (-2, -1),
            (+2, -1),
            (-1, -2),
            (+1, -2),
        ]
        file_num, rank_num = square_to_file_rank(square)
        for file_step, rank_step in knights_moves:
            new_file = file_num + file_step
            new_rank = rank_num + rank_step
            if not on_board(new_file, new_rank):
                continue
            new_square = file_rank_to_square(new_file, new_rank)
            if self.is_own_piece(new_square,layout):
                continue
            else:
                moveable_spaces.append(new_square)
        return moveable_spaces

class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "bishop")

class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "rook")

class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "queen")

class King(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "king")
