from coords import *
from directions import *


class Piece:
    def __init__(self, color, kind) -> None:
        self.color = color
        self.kind = kind
        self.has_moved = False

    def is_own_piece(self, square, layout) -> bool:
        piece = layout[square]
        return piece is not None and piece.color == self.color

    def get_moves(self, square, layout) -> list[str]:
        moveable_spaces: list[str] = []
        return moveable_spaces

    def get_attacks(self, square, layout):
        return self.get_moves(square, layout)

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

    def get_attacks(self, square, layout):
        attacked_spaces: list[str] = []
        file_num, rank_num = square_to_file_rank(square)
        if self.color == "white":
            direction = +1
        else:
            direction = -1
        new_rank = rank_num + direction
        for step in [-1, +1]:
            attack_file = file_num + step
            if not on_board(attack_file, new_rank):
                continue
            attack_square = file_rank_to_square(attack_file, new_rank)
            attacked_spaces.append(attack_square)
        return attacked_spaces


    def get_moves(self,square,layout, en_passant_square = None) -> list[str]:
        moveable_spaces: list[str] = []
        file_num, rank_num = square_to_file_rank(square)
        if self.color == "white":
            direction = +1
            start_rank = 2
        else:
            direction = -1
            start_rank = 7
        new_rank = rank_num + direction
        if not on_board(file_num, new_rank):
            return moveable_spaces
        new_square = file_rank_to_square(file_num, new_rank)
        if layout[new_square] is None:
            moveable_spaces.append(new_square)
            if start_rank == rank_num:
                start_direction = direction * 2
                new_start_rank = rank_num + start_direction
                new_start_square = file_rank_to_square(file_num, new_start_rank)
                if layout[new_start_square] is None:
                    moveable_spaces.append(new_start_square)
        captureable_steps = [-1, +1]
        for step in captureable_steps:
            capture_file = file_num + step
            if not on_board(capture_file, new_rank):
                continue
            new_captured_square = file_rank_to_square(capture_file, new_rank)
            if self.is_own_piece(new_captured_square,layout):
                continue
            if layout[new_captured_square] is None and new_captured_square != en_passant_square:
                continue
            moveable_spaces.append(new_captured_square)
        return moveable_spaces





class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "knight")

    def get_moves(self, square, layout) -> list[str]:
        return self.slide_moves(square, layout, KNIGHTS_MOVES, False)

class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "bishop")

    def get_moves(self, square, layout) -> list[str]:
        return self.slide_moves(square, layout, BISHOPS_MOVES, True)

class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "rook")

    def get_moves(self, square, layout) -> list[str]:
        return self.slide_moves(square, layout, ROOKS_MOVES, True)

class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "queen")

    def get_moves(self, square, layout) -> list[str]:
        return self.slide_moves(square, layout, QUEENS_MOVES, True)


class King(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "king")

    def get_moves(self, square, layout) -> list[str]:
        return self.slide_moves(square, layout, KINGS_MOVES, False)
