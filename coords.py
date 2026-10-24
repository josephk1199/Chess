from constants import *


def square_to_pixels(square) -> tuple[int, int]:
    file_id = FILES.index(square[0])
    rank_id = BOARD_SIZE - int(square[1])
    x = file_id * SQUARE_SIZE
    y = rank_id * SQUARE_SIZE

    return x, y

def pixels_to_square(pos) -> str:
    x, y = pos
    file_id = x // SQUARE_SIZE
    rank_id = y // SQUARE_SIZE
    file = FILES[file_id]
    rank = BOARD_SIZE - rank_id
    rank = str(rank)
    result = file + rank
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
