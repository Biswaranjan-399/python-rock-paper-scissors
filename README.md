# 🗿✂️ Stone Paper Scissors (Terminal Game)

A simple, terminal-based implementation of the classic Stone, Paper, Scissors game written in Python.

## 🚀 How to Run the Game

### Prerequisites

You only need **Python 3** installed on your machine.

### Execution

1. **Clone the Repository** (or ensure the `game.py` file is on your computer).

2. Open your **terminal** or **command prompt**.

3. Navigate to the directory where the file is located.

4. Run the game using the Python interpreter

(Note: Replace `your_filename.py` with the actual name of your Python file, e.g., `sps_game.py`).

### Gameplay

The game will prompt you to enter your choice using single letters:

- **r** for Rock (Stone)

- **p** for Paper

- **s** for Scissors

The computer's choice will be displayed, and the result will be announced instantly.

## 🛠️ Features

- **Simple Interface:** Runs directly in the terminal, requiring no dependencies outside of standard Python.

- **Randomized Computer Choice:** Uses the `random` module to ensure fair play.

- **Clear Results:** Immediately displays both choices and the outcome (Win, Lose, or Draw).

## 💡 Logic Explained

The core of the game uses an elegant numerical mapping system to determine the winner:

| Choice       | Numerical Value |
| ------------ | --------------- |
| **Rock**     | `1`             |
| **Paper**    | `0`             |
| **Scissors** | `-1`            |

The program compares the user's value and the computer's value based on win/loss conditions (e.g., Rock `1` beats Scissors `-1`) to resolve the match efficiently.

## 🤝 Contributing

Feel free to fork this repository if you want to add features like score tracking, multiple rounds, or a GUI.
