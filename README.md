# Console-Based War Game

Welcome to the Console-Based War Game! This is a text-based strategy game where two players purchase different units and engage in battles across various terrains.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)

## Features

- **Multiple Unit Types**: Choose from troops, artillery, and tanks, each with different costs and values.
- **Resource Management**: Start with a fixed amount of money and strategize your purchases.
- **Terrain Effects**: Battles are influenced by the terrain, adding an extra layer of strategy.
- **Battle System**: Engage in multiple battles to determine the ultimate winner.

## Installation

To run the game, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/robkoocz/consoleWarGame.git
   cd consoleWarGame
   ```
2. Ensure you have Python installed (version 3.6 or later).

3. Run the game:

    ```sh
    python main.py
    ```

## How to Play
1. Each player starts with a fixed amount of money.
2. Players take turns to purchase units (troops, artillery, tanks).
3. After purchasing units, players engage in battles on randomly selected terrains.
4. The game conducts multiple battles, and the player with the most units at the end wins.

## Project Structure
```
war_game/
│
├── main.py        # Entry point of the game
├── game.py        # Main game logic
├── units.py       # Unit definitions and factory
├── player.py      # Player class and methods
├── battle.py      # Battle mechanics
└── terrain.py     # Terrain effects
```
## Future improvements

- Better fighting mechanics
- More terrains and units
- Random events
- More beautiful UI inside the console (colors, spaces)