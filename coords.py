from constants import *


def square_to_pixels(square):
    file_id = FILES.index(square[0])
    rank_id = BOARD_SIZE - int(square[1])
    x = file_id * SQUARE_SIZE
    y = rank_id * SQUARE_SIZE

    return x, y

def pixels_to_square(pos):
    x, y = pos
    file_id = x // SQUARE_SIZE
    rank_id = y // SQUARE_SIZE
    file = FILES[file_id]
    rank = BOARD_SIZE - rank_id
    rank = str(rank)
    result = file + rank
    return result
