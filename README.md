# Hangman Game

A simple command-line Hangman game implemented in Python.

## Description

This project is a text-based implementation of the classic Hangman game. The player must guess a hidden word letter by letter. For each incorrect guess, they lose one life. The game ends when either the player successfully guesses the word or runs out of lives.

## Features

- Random word selection from a predefined list
- Input validation to ensure proper gameplay
- Visual display of correctly and incorrectly guessed letters
- Turn and error counting
- Win and lose conditions

## Installation

1. Clone this repository:
   ```[
   git clone https://github.com/w555219/hangman.git
   ```

2. Navigate to the project directory:
   ```
   cd hangman
   ```

3. No additional dependencies are required as this project uses only Python standard libraries.

## Usage

To start the game, run:
```
python main.py
```

Follow the on-screen instructions to play:
1. The game displays the hidden word as underscores
2. Enter one letter per turn
3. The game will show if your guess was correct or not
4. Continue guessing until you either:
   - Find all the letters in the word (you win)
   - Run out of lives (you lose)

## Project Structure

```
hangman/
│
├── draft/           # Draft implementation
│   └── draft.py
├── utils/           # Game logic
│   └── game.py  
├── main.py          # Entry point
└── README.md        # This file
```

## Visual ASCII Representation

Below is a simple visual representation of the hangman that could be added to enhance the game:

```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

## Contributors

- WASEEM ALNALOUTI

## Timeline

- Project started: [1/4/2025]
- Project completed: [3/4/2025]

## Personal Situation

This project was created as a learning exercise to practice object-oriented programming in Python.
