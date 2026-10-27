from constants import *


def square_to_pixels(square, flipped = False) -> tuple[int, int]:
    file, rank = square_to_file_rank(square)
    if flipped:
        col = (BOARD_SIZE - 1) - file
        row = rank - 1
    else:
        col = file
        row = BOARD_SIZE - rank
    x = col* SQUARE_SIZE
    y = row * SQUARE_SIZE
    return x, y

def pixels_to_square(pos, flipped = False) -> str:
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    if flipped:
        file_id = (BOARD_SIZE - 1) - col
        rank_num = row + 1
    else:
        file_id = col
        rank_num = BOARD_SIZE - row
    file = FILES[file_id]
    result = file + str(rank_num)
    return result

def square_to_file_rank(square) -> tuple[int, int]:
    file_id = FILES.index(square[0])
    rank_id = int(square[1])
    return file_id, rank_id

def file_rank_to_square(file_id, rank_id) -> str:
    file = FILES[file_id]
    rank = str(rank_id)
    result = file + rank
    return result

def on_board(file_id, rank_id) -> bool:
    return 0 <= file_id <= 7 and 1 <= rank_id <= 8
