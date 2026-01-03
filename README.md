# Agent

Implementation of intelligent agents for different environments.

## Overview

This repository contains implementations of intelligent agents that can interact with and solve tasks in different environments:

- **Vacuum Agent** (`vacuum.py`): A reactive and planning-based vacuum cleaner agent that can clean dirty locations and navigate obstacles intelligently

## Files

- `vacuum.py` - Vacuum world environment with intelligent cleaning agent
- `README.md` - This documentation file

## Getting Started

### Prerequisites

- Python 3.7 or higher
- tkinter (usually included with Python)

### Running the Agent

```bash
python vacuum.py
```

This will launch a GUI window showing the vacuum agent in action, with real-time visualization of the cleaning process.

## Agent Architecture

### Vacuum Agent Features

- **Intelligent Navigation**: Moves efficiently through the environment
- **Obstacle Avoidance**: Detects and avoids obstacles
- **Dirt Detection**: Identifies and cleans dirty locations
- **Multiple Strategies**: Supports both reactive and planning-based approaches
- **Visual Feedback**: Real-time GUI showing agent state and environment

### Agent Components

1. **VacuumAgent Class**: The intelligent agent with decision-making capabilities
2. **Room Class**: The environment representing the space to be cleaned
3. **GUI Visualization**: Interactive display using tkinter

### Algorithms

- **Reactive Agent**: Makes decisions based on immediate observations
- **Planning Agent**: Uses search algorithms to find optimal cleaning paths
- **Obstacle Handling**: Implements collision detection and path finding

## Environment Details

- **Grid-based Room**: Configurable grid size for various room layouts
- **Cell Types**: Clean, dirty, obstacles, and agent position
- **Dynamic Obstacles**: Can handle fixed obstacles and dynamic elements
- **Performance Metrics**: Tracks moves and cleaning efficiency

## How to Use

1. Run the vacuum agent: `python vacuum.py`
2. Watch as the agent navigates the room and cleans dirty areas
3. The GUI displays:
   - Agent position and direction
   - Dirty locations
   - Obstacles
   - Cleaning progress
   - Movement statistics

## Performance Metrics

The agent tracks:
- Total moves made
- Cells cleaned
- Cleaning efficiency
- Path optimization

## Customization

You can modify:
- Room dimensions
- Dirt distribution
- Obstacle placement
- Agent strategy and behavior
- GUI appearance

## Future Enhancements

- Multi-agent coordination
- Learning-based strategies
- Different room layouts
- Advanced pathfinding algorithms
- Performance optimization

## License

MIT License