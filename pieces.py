class Piece:
    def __init__(self, color, kind) -> None:
        self.color = color
        self.kind = kind

class Pawn(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "pawn")

class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, "knight")

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
