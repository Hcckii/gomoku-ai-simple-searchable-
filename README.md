# Gomoku AI

A fully playable Gomoku (Five in a Row) game with an AI opponent, built in Python using the Processing framework.

-----

## About

Gomoku is a classic strategy board game where the goal is to place five stones in a row — horizontally, vertically, or diagonally. This implementation features a custom-built AI with three difficulty levels and smooth stone placement animations.

-----

## Features

- Human vs AI gameplay on a standard board
- Three AI difficulty levels (Noob / Beginner / Master)
- Animated stone placement
- Win detection across all four directions (horizontal, vertical, two diagonals)
- Modular codebase with unit tests for all non-graphical logic

-----

## Tech Stack

- Python
- Processing (via Python Mode)

-----

## How to Run

1. Install [Processing3] https://github.com/processing/processing/releases with Python Mode enabled
1. Clone this repository
1. Open the main `.pyde` file in Processing
1. Press **Run**

-----

## AI Design

The AI behavior changes significantly across difficulty levels:

### Noob

- Only blocks when the player has **4 stones in a row** (almost winning)
- Otherwise plays offensively near its own existing stones
- Winrate against a decent player: ~20%

### Beginner

- Blocks threats earlier (3+ stones in a row)
- Tries to win if a winning move is available
- Picks randomly from the **top 3 scored positions** to add unpredictability
- Winrate: roughly 50/50

### Master

- Uses a full `find_best_move()` evaluation:
1. Checks if the AI can win in one move → plays it
1. Checks if the player can win in one move → blocks it
1. Scores every available position using `evaluate_position()` → plays the highest score
- `evaluate_position` scoring:
  - 4 stones in a line: **10,000 pts**
  - 3 stones in a line: **1,000 pts**
  - 2 stones in a line: **100 pts**
  - Blocked line (opponent stone at end): **0 pts**
  - Center proximity: bonus points
- Winrate against the player: ~60–70%

### Known Limitations

- Does not detect **double threats** (two ways to win simultaneously)
- Looks only **one move ahead** — no minimax yet

### Future Improvements

- Implement minimax with alpha-beta pruning for multi-move lookahead
- Detect and prioritize double threats / forks
- Differentiate open-ended vs blocked lines in evaluation
- Add an opening book for early game strategy

-----

## Project Structure

```
gomoku-ai/
├── gomoku.pyde       # Main game loop
├── ai.py             # AI logic and move selection
├── win_check.py      # Win detection across all directions
├── constants.py      # Board configuration and shared state
├── test_ai.py        # Unit tests for AI logic
├── test_win_check.py # Unit tests for win detection
└── ai.txt            # AI design notes
```

-----

## Testing

```bash
pytest test_ai.py test_win_check.py
```

All tests cover non-graphical logic only and are fully isolated from game state.
