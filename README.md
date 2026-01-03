# Tic Tac Toe Game with AI Agent

An intelligent Tic Tac Toe game implementation featuring an AI opponent that uses the Minimax algorithm with alpha-beta pruning for optimal decision-making.

## Overview

This project implements a complete Tic Tac Toe game with:
- **AI Agent**: Unbeatable AI opponent using Minimax algorithm
- **Heuristic Evaluation**: Smart board evaluation using the heuristic function e(p)
- **Optimal Play**: Alpha-beta pruning for efficient game tree search
- **Interactive GUI**: User-friendly interface to play against the AI
- **Game Analysis**: Detailed heuristic calculations displayed during gameplay

## Files

- `Tic_Tac_Toe.py` - Complete game implementation with AI agent
- `README.md` - This documentation file

## Features

### Core Game Features
- **Human vs AI**: Play against an intelligent computer opponent
- **Perfect AI**: The AI never loses (always wins or forces a draw)
- **Real-time Analysis**: Displays heuristic values and game evaluations
- **Interactive Board**: Click to make your moves
- **Game History**: Track all moves and evaluations

### AI Features
- **Minimax Algorithm**: Explores all possible game states
- **Alpha-Beta Pruning**: Optimizes search by eliminating unnecessary branches
- **Heuristic Evaluation**: Uses e(p) = (Player Open Lines) - (Opponent Open Lines)
- **Depth-First Search**: Efficient game tree traversal
- **Winning Prediction**: Identifies winning/losing positions in advance

## Getting Started

### Prerequisites

- Python 3.7 or higher
- tkinter (usually included with Python)

### Running the Game

```bash
python Tic_Tac_Toe.py
```

This will launch the game GUI where you can play against the AI.

## How to Play

1. **Start Game**: Click "New Game" or launch the application
2. **Make Your Move**: Click on any empty cell (X is your symbol)
3. **AI Response**: The AI (O) automatically responds with its optimal move
4. **Win Condition**: First player to get 3 in a row, column, or diagonal wins
5. **Draw**: If the board fills and no winner emerges
6. **Play Again**: Click "New Game" to start a fresh match

## Game Mechanics

### Board Representation
```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

### Winning Conditions
- **3 in a Row**: Horizontal lines (rows 1-3, 4-6, 7-9)
- **3 in a Column**: Vertical lines (columns 1-4-7, 2-5-8, 3-6-9)
- **3 in a Diagonal**: Both diagonals (1-5-9 and 3-5-7)

## AI Algorithm Details

### Minimax Algorithm

The AI uses the Minimax algorithm to evaluate all possible game states:

1. **Generate States**: Recursively explore all possible moves
2. **Evaluate Terminal States**: Check for wins, losses, or draws
3. **Backtrack Scores**: Propagate scores up the game tree
4. **Choose Best Move**: Select move with highest score

### Heuristic Function: e(p)

The board evaluation uses the heuristic:
```
e(p) = (Lines open for Player) - (Lines open for Opponent)
```

**Winning Lines**: 8 total (3 rows + 3 columns + 2 diagonals)

**Open Line**: A line that contains:
- No opponent pieces (player can still win this line)
- At least one player piece (player has potential)

### Algorithm Pseudocode

```
function minimax(board, depth, isMaximizing):
    if game_over(board):
        return evaluate(board)
    
    if isMaximizing:  // AI's turn (maximize)
        bestScore = -infinity
        for each move:
            score = minimax(board with move, depth+1, false)
            bestScore = max(score, bestScore)
        return bestScore
    else:             // Player's turn (minimize)
        bestScore = +infinity
        for each move:
            score = minimax(board with move, depth+1, true)
            bestScore = min(score, bestScore)
        return bestScore
```

### Alpha-Beta Pruning

Optimization technique that reduces the number of nodes evaluated:
- **Alpha**: Best score for maximizer
- **Beta**: Best score for minimizer
- **Pruning**: Skip branches where alpha >= beta

## Example Game State Analysis

### Sample Board:
```
 X | - | -
-----------
 - | O | -
-----------
 X | - | -
```

### Heuristic Calculation for Player 'X':
- **Player (X) open lines**: 2 (column 1, left diagonal)
- **Opponent (O) open lines**: 0
- **e(p)** = 2 - 0 = **2** (Favorable for X)

## Game States

### Winning States
- Player has 3 in a line: **Evaluation = +10**

### Losing States
- Opponent has 3 in a line: **Evaluation = -10**

### Draw States
- Board full, no winner: **Evaluation = 0**

### Intermediate States
- Calculated using heuristic function e(p)

## Performance

### Time Complexity
- **Worst Case**: O(9!) ≈ 362,880 nodes
- **With Alpha-Beta**: Average 10,000-50,000 nodes

### Space Complexity
- O(depth) = O(9) for recursion stack

### Move Decision Time
- Typically < 1 second for optimal move selection

## Technical Implementation

### Main Components

1. **Board Class**: Manages game state
   - Position tracking
   - Move validation
   - Win/draw detection

2. **AI Agent Class**: Implements Minimax
   - Game tree search
   - Heuristic evaluation
   - Move selection

3. **GUI Class**: Interactive interface
   - Board visualization
   - Move input handling
   - Game status display

### Key Methods

- `minimax(board, depth, isMaximizing)`: Core algorithm
- `evaluate(board)`: Terminal state evaluation
- `calculate_heuristic(board, player)`: Intermediate state evaluation
- `get_best_move(board)`: AI decision making
- `is_winning(board, player)`: Win condition check

## Gameplay Tips

### For Players
- **Center is Powerful**: The middle cell (5) is involved in 4 winning lines
- **Corners Matter**: Corner cells (1,3,7,9) are involved in 3 winning lines
- **Block Smartly**: Always block opponent's winning moves when possible

### Against This AI
- The AI is unbeatable with perfect play
- The best outcome is a draw
- This demonstrates optimal game-playing agents

## Customization Options

You can modify:
- AI difficulty (implement limited search depth)
- Heuristic function weights
- Board size (generalize to 4x4, 5x5, etc.)
- GUI appearance and colors
- Game speed

## Future Enhancements

- **Difficulty Levels**: Implement limited search depth for easier gameplay
- **Game Variants**: Gomoku, Connect Four, larger boards
- **Machine Learning**: Train neural network to learn evaluation function
- **Move Annotations**: Show AI's thinking and evaluation scores
- **Tournament Mode**: Play multiple games with statistics
- **Network Play**: Online multiplayer support
- **Opening Library**: Use predefined opening strategies

## Educational Value

This implementation demonstrates:
- **Game Theory**: Minimax algorithm and game tree search
- **Algorithm Optimization**: Alpha-beta pruning
- **Heuristic Functions**: Board evaluation strategies
- **Artificial Intelligence**: Decision-making under uncertainty
- **Python Programming**: Class design and GUI development
- **Recursion**: Deep game tree traversal

## References

- Minimax Algorithm: https://en.wikipedia.org/wiki/Minimax
- Alpha-Beta Pruning: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- Game Theory: https://en.wikipedia.org/wiki/Game_theory
- Adversarial Search: Russell & Norvig - Artificial Intelligence: A Modern Approach

## Author

Agent Repository - Tic Tac Toe Implementation

## License

MIT License