# AI Agent Repository

Collection of intelligent agent implementations demonstrating various AI algorithms and problem-solving techniques.

## Overview

This repository contains three AI agent projects:
1.**Tic Tac Toe AI** - Game-playing agent using Minimax algorithm
2. **Block World AI** - Planning agent using STRIPS-like algorithm with BFS
3. **Vacuum World AI** - Autonomous cleaning agent with reactive and planning strategies

## Files

- `Tic_Tac_Toe.py` - Tic Tac Toe game with unbeatable AI opponent
- `Block_World.py` - Block World problem solver with GUI visualization
- `vacuum.py` - Vacuum cleaning agent with autonomous navigation
- `README.md` - This documentation file

---

## 1. Tic Tac Toe Game (Tic_Tac_Toe.py)

**Description**: Interactive game with perfect-play AI using adversarial search.

**Key Features**:
- Unbeatable AI opponent using Minimax with alpha-beta pruning
- Heuristic evaluation: e(p) = (Player Open Lines) - (Opponent Open Lines)
- Real-time board analysis and game state evaluation
- Interactive GUI for human vs AI gameplay

**Algorithm**: Minimax with Alpha-Beta Pruning
- Explores all possible game states
- Prunes unnecessary branches for efficiency
- Guarantees optimal play (AI never loses)

**How to Run**:
```bash
python Tic_Tac_Toe.py
```

**Complexity**: O(9!) worst case, optimized to ~10k-50k nodes with pruning

---

## 2. Block World AI (Block_World.py)

**Description**: STRIPS-like planning agent that solves Block World rearrangement problems.

**Key Features**:
- BFS-based planning to find optimal action sequences
- Autonomous goal achievement with multiple predefined goals
- Visual GUI showing blocks and robot arm movements
- Actions: pick_up, put_down, stack, unstack

**Algorithm**: Breadth-First Search (BFS)
- Explores state space to find goal state
- Tracks visited states to avoid cycles
- Returns shortest action sequence

**Problem Setup**:
- Initial: 3 blocks (A, B, C) in specific configuration
- Goals: Build towers, rearrange blocks, all on table

**How to Run**:
```bash
python Block_World.py
```

**Complexity**: O(b^d) where b=branching factor, d=solution depth

---

## 3. Vacuum World AI (vacuum.py)

**Description**: Autonomous cleaning agent navigating a grid environment with obstacles.

**Key Features**:
- Intelligent navigation and pathfinding
- Obstacle detection and avoidance
- Dirt detection and cleaning
- Performance metrics tracking
- Real-time GUI visualization

**Algorithm**: Reactive + Planning Agent
- Reactive: Responds to immediate observations
- Planning: Uses search for optimal cleaning paths
- Handles dynamic and static obstacles

**Environment**:
- Grid-based room with configurable size
- Cell types: clean, dirty, obstacles
- Agent tracks position and direction

**How to Run**:
```bash
python vacuum.py
```

**Performance Metrics**: Moves, cells cleaned, efficiency

---

---

## Technical Comparison

| Feature | Tic Tac Toe | Block World | Vacuum World |
|---------|-------------|-------------|--------------|
| **Algorithm** | Minimax | BFS Planning | Reactive/Planning |
| **Search Type** | Adversarial | State Space | Pathfinding |
| **Optimization** | Alpha-Beta | Visited Set | Heuristic |
| **Domain** | Game Playing | Planning | Navigation |
| **State Space** | 9! states | Exponential | Grid-based |
| **GUI** | Yes | Yes | Yes |

## Prerequisites

- Python 3.7 or higher
- tkinter (included with Python)

## Quick Start

Run any agent:
```bash
python Tic_Tac_Toe.py    # Play Tic Tac Toe
python Block_World.py     # Watch Block World solver
python vacuum.py          # Run Vacuum cleaner
```

## AI Concepts Demonstrated

### 1. **Adversarial Search** (Tic Tac Toe)
- Game tree exploration
- Min-Max decision making
- Alpha-beta pruning optimization
- Heuristic evaluation functions

### 2. **Automated Planning** (Block World)
- STRIPS operators (preconditions, effects)
- Goal-driven action selection
- State space search
- Optimal plan generation

### 3. **Autonomous Agents** (Vacuum World)
- Perception-action cycle
- Reactive decision making
- Environment modeling
- Performance measurement

## Learning Outcomes

This repository demonstrates:
- **Search Algorithms**: BFS, Minimax, pathfinding
- **AI Techniques**: Planning, game playing, autonomous agents
- **Optimization**: Alpha-beta pruning, visited sets, heuristics
- **Python Skills**: OOP, GUI development, algorithm implementation
- **Problem Solving**: State representation, action modeling, goal achievement

## Future Enhancements

- **Tic Tac Toe**: Neural network learning, larger boards (Gomoku)
- **Block World**: A* search, more complex goals, multiple arms
- **Vacuum World**: Multi-agent coordination, learning-based navigation

## References

- Russell & Norvig - *Artificial Intelligence: A Modern Approach*
- Minimax Algorithm: https://en.wikipedia.org/wiki/Minimax
- STRIPS Planning: https://en.wikipedia.org/wiki/STRIPS
- Intelligent Agents: https://en.wikipedia.org/wiki/Intelligent_agent

## Author

Agent Repository - AI Implementations

## License

MIT License