KNIGHTS_MOVES = [
    (-1, +2),
    (+1, +2),
    (-2, +1),
    (+2, +1),
    (-2, -1),
    (+2, -1),
    (-1, -2),
    (+1, -2),
]

BISHOPS_MOVES = [
    (+1, +1),
    (-1, -1),
    (+1, -1),
    (-1, +1),
]

ROOKS_MOVES = [
     (0, +1),
     (0, -1),
     (+1, 0),
     (-1, 0),
 ]

QUEENS_MOVES = BISHOPS_MOVES + ROOKS_MOVES

KINGS_MOVES = QUEENS_MOVES
