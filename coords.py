from constants import *


def square_to_pixels(square):
    file_id = FILES.index(square[0])
    rank_id = BOARD_SIZE - int(square[1])
    x = file_id * SQUARE_SIZE
    y = rank_id * SQUARE_SIZE

    return x, y

def pixels_to_square():
    pass
