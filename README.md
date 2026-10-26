# Chess

A two-player chess game written in Python with [pygame](https://www.pygame.org/). Both players share one window and take turns by clicking pieces on the board. The full rules of chess are implemented: every piece's movement, check, checkmate, stalemate, castling, en passant, and pawn promotion.

## What it does

- Draws an 8×8 board with piece images and runs at 60 FPS
- Click one of your pieces to select it; the square turns yellow and every **legal** move is marked with a dot
- Click a dotted square to move there, or click the piece again to deselect it
- Only legal moves are offered: you can never leave your own king in check, so pinned pieces and moves into check are filtered out automatically
- **Castling** kingside and queenside, as long as neither the king nor that rook has moved, the squares between them are empty, and the king isn't in, passing through, or landing on check
- **En passant** captures, available only on the move immediately after an enemy pawn's two-square advance
- **Pawn promotion**: when a pawn reaches the last rank a menu pops up and you choose a queen, rook, bishop, or knight
- **Checkmate** and **stalemate** are detected after every move and a game-over panel appears with a **NEW GAME** button
- Press **⌘ R** (Mac) at any time to start a new game

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- pygame 2.6.1 (installed automatically below)

## Clone and run

```bash
git clone https://github.com/josephk1199/Chess.git
cd Chess
uv run main.py
```

`uv run` creates a virtual environment, installs pygame from `uv.lock`, and launches the game in one step.

If you don't use uv:

```bash
git clone https://github.com/josephk1199/Chess.git
cd Chess
python3 -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install pygame==2.6.1
python main.py
```

Run it from the repository root; the piece images are loaded from the `assets/` folder using a relative path.

## How to play

1. White moves first. Click a white piece, then click one of the dotted squares.
2. Turns alternate automatically. Clicking an enemy piece does nothing until it's that side's turn.
3. To castle, click the king and then the square two files toward the rook (`g1`/`c1` for White, `g8`/`c8` for Black). The rook jumps over on its own.
4. When a pawn reaches the far side, pick a piece from the promotion menu to continue.
5. When the game ends, click **NEW GAME** on the panel (or press **⌘ R**) to reset the board.

## Project structure

| File | What it does |
|------|--------------|
| `main.py` | Entry point. Sets up the pygame window, runs the event loop, and redraws the board every frame. |
| `constants.py` | Board dimensions, colors, square size, and other settings in one place. |
| `board.py` | Builds the starting position as a dictionary mapping squares (`"e4"`) to pieces, and resets all game state for a new game. |
| `pieces.py` | The `Piece` base class and one subclass per piece type. Each piece knows how to generate its own raw moves and the squares it attacks. |
| `directions.py` | The step patterns (file, rank offsets) for knights, bishops, rooks, queens, and kings. |
| `rules.py` | The chess rules layer: detects attacked squares, finds kings, filters raw moves down to legal moves by simulating each one, handles castling, and decides whether the game is still going, checkmate, or stalemate. |
| `click.py` | Translates mouse clicks into selecting, moving, capturing, castling, en passant, and promotion. |
| `coords.py` | Converts between pixel positions, square names like `"e4"`, and numeric file/rank indexes. |
| `draw_board.py` | Everything that gets drawn: squares, piece images, selection highlight, move dots, the game-over panel, and the promotion menu. |
| `assets/` | PNG images for all twelve pieces. |

## How it works

The board is a plain dictionary with 64 keys (`"a1"` through `"h8"`) whose values are either a piece object or `None`. Each piece class (`Pawn`, `Knight`, `Bishop`, `Rook`, `Queen`, `King`) inherits from `Piece` and overrides `get_moves()`. Sliding pieces share one `slide_moves()` helper that walks outward in each direction until it hits the edge of the board or another piece.

Raw moves are not the same as legal moves. `rules.legal_moves()` takes each candidate move, plays it on the board, checks whether the moving side's king is now attacked, and then undoes the move. Only the moves that don't leave the king in check are returned, which is what gives the game correct handling of pins, checks, and forced responses without any special-case code.

After every move `rules.game_status()` asks whether the side to move has any legal moves left. If it does, play continues; if it doesn't, the game is checkmate when the king is attacked and stalemate when it isn't.

## Not implemented (yet)

- Draw by threefold repetition, the fifty-move rule, or insufficient material
- Move history / algebraic notation
- Undo
- Chess clocks
- A computer opponent
