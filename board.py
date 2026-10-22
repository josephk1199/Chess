from constants import FILES, RANKS


def fill_board():
    board_dict = {}
    for file in FILES:
        for rank in RANKS:
            board_dict[file + rank] = None
    return board_dict
