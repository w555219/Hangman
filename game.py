# utils/game.py
import random
from typing import List


class Hangman:
    """
    A class representing the Hangman game.
    
    This class contains all the necessary functionality for a Hangman game,
    including word selection, guess processing, and game state management.
    """
    
    def __init__(self) -> None:
        """
        Initialize a new Hangman game with default settings.
        """
        # List of possible words to choose from
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        
        # Select a random word and convert to list of characters
        self.word_to_find: List[str] = list(random.choice(self.possible_words))
        
        # Player starts with 5 lives
        self.lives: int = 5
        
        # Initialize correctly guessed letters with underscores
        self.correctly_guessed_letters: List[str] = ['_' for _ in self.word_to_find]
        
        # Initialize wrongly guessed letters as empty list
        self.wrongly_guessed_letters: List[str] = []
        
        # Initialize turn count
        self.turn_count: int = 0
        
        # Initialize error count
        self.error_count: int = 0
    
    def play(self) -> None:
        """
        Handle one turn of the game, asking the player for a letter guess
        and updating the game state accordingly.
        """
        # Increment turn counter
        self.turn_count += 1
        
        # Ask player for input until valid
        while True:
            guess = input("Enter a letter: ").lower()
            
            # Validate input: must be a single letter
            if len(guess) != 1:
                print("Please enter exactly one letter.")
                continue
            
            if not guess.isalpha():
                print("Please enter a letter (a-z).")
                continue
            
            # Check if letter has already been guessed
            if (guess in self.correctly_guessed_letters or 
                guess in self.wrongly_guessed_letters):
                print("You already guessed that letter. Try another one.")
                continue
            
            # Valid input received
            break
        
        # Process the guess
        if guess in self.word_to_find:
            # Update correctly guessed letters
            for i, letter in enumerate(self.word_to_find):
                if letter == guess:
                    self.correctly_guessed_letters[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            # Update wrongly guessed letters
            self.wrongly_guessed_letters.append(guess)
            self.lives -= 1
            self.error_count += 1
            print(f"Wrong guess! '{guess}' is not in the word. You lost a life!")
    
    def start_game(self) -> None:
        """
        Start the Hangman game and continue until the player wins or loses.
        """
        print("Welcome to Hangman!")
        print(f"Try to guess the word: {' '.join(self.correctly_guessed_letters)}")
        
        # Continue while player has lives and word is not completely guessed
        while self.lives > 0 and '_' in self.correctly_guessed_letters:
            # Play one turn
            self.play()
            
            # Display current game state
            print(f"Word: {' '.join(self.correctly_guessed_letters)}")
            print(f"Wrong guesses: {', '.join(self.wrongly_guessed_letters)}")
            print(f"Lives: {self.lives}")
            print(f"Errors: {self.error_count}")
            print(f"Turn count: {self.turn_count}")
            print("-" * 30)
            
            # Check if game is over
            if self.lives == 0:
                self.game_over()
                break
            
            # Check if word is found
            if '_' not in self.correctly_guessed_letters:
                self.well_played()
                break
    
    def game_over(self) -> None:
        """
        Display game over message when player runs out of lives.
        """
        print("Game over...")
        print(f"The word was: {''.join(self.word_to_find)}")
    
    def well_played(self) -> None:
        """
        Display congratulation message when player correctly guesses the word.
        """
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
        from utils.game import Hangman




