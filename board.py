from constants import FILES, RANKS
from pieces import *


def fill_board():
    board_dict = {}
    for file in FILES:
        for rank in RANKS:
            board_dict[file + rank] = None
    for file in FILES:
        board_dict[file + "2"] = Pawn("white")
        board_dict[file + "7"] = Pawn("black")
    piece_types = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    for file, piece_type in zip(FILES, piece_types):
        board_dict[file + "1"] = piece_type("white")
        board_dict[file + "8"] = piece_type("black")

    return board_dict
