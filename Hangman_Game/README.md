# Hangman Game (Python CLI)

A simple command-line implementation of the classic Hangman game written in Python.  
The player has to guess the secret word, one letter at a time, before running out of attempts.

---

## How to Play
1. The program randomly selects a word from a predefined list.
2. The player has a limited number of attempts (equal to the word length).
3. Each correct guess reveals the letter(s) in the word.
4. Each incorrect guess reduces the number of remaining attempts.
5. The game ends when:
   - The player correctly guesses all the letters (win).
   - The player runs out of attempts (lose).

---

## Features
- Input validation (only single letters allowed).
- Case-insensitive guesses.
- Dynamic progress display (`_` for unknown letters).
- Word list includes popular tech companies.

---

## Requirements
- Python 3.x installed on your system.

---

## Run the Game
Clone or download this project, then run:

```bash
python main.py ```

or

```bash
python3 main.py ```

## Gameplay 
```You have 7 attempts to guess the right word
   _ _ _ _ _ _ _
   > 1: Enter the right letter: a
   You have 7 attempts to guess the right word
   _ a _ a _ _ _

   ...