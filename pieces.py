from coords import *


class Piece:
    def __init__(self, color, kind) -> None:
        self.color = color
        self.kind = kind

    def is_own_piece(self, square, layout) -> bool:
        piece = layout[square]
        return piece is not None and piece.color == self.color

    def get_moves(self, square, layout) -> list[str]:
        moveable_spaces: list[str] = []
        return moveable_spaces

    def slide_moves(self, square, layout, steps, slide):
        moveable_spaces: list[str] = []
        file_num, rank_num = square_to_file_rank(square)
        for file_step, rank_step in steps:
            current_file = file_num
            current_rank = rank_num
            while True:
                current_file = current_file + file_step
                current_rank = current_rank + rank_step
                if not on_board(current_file, current_rank):
                    break
                new_square = file_rank_to_square(current_file, current_rank)
                if self.is_own_piece(new_square,layout):
                    break
                moveable_spaces.append(new_square)
                if layout[new_square] is not None:
                    break
                if not slide:
                    break
        return moveable_spaces

class Pawn(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "pawn")



class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "knight")

    def get_moves(self, square, layout) -> list[str]:
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
        return self.slide_moves(square, layout, knights_moves, False)

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

    def get_moves(self, square, layout) -> list[str]:
        kings_moves = [
            (-1, +1),
            (0, +1),
            (+1, +1),
            (-1, 0),
            (+1, 0),
            (-1, -1),
            (0, -1),
            (+1, -1),
        ]
        return self.slide_moves(square, layout, kings_moves, False)
