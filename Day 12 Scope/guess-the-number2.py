#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing game!")

secretNumber = random.randint(1, 100)
print("I am thinking in a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
  for guessesTaken in range(10, 0, -1):
    print('You have ' + str(guessesTaken) + ' attempts remaining to guess the number!')
    guess = int(input("Make a guess: "))
    if guess < secretNumber:
      print("Too low.")
      print("Guess again")
    elif guess > secretNumber:
      print("Too high.")
      print("Guess again")
    else:
      break #This condition is the correct  guess
elif level == "hard":
  for guessesTaken in range(5, 0, -1):
    print('You have ' + str(guessesTaken) + ' attempts remaining to guess the number!')
    guess = int(input("Make a guess: "))
    if guess < secretNumber:
      print("Too low.")
      print("Guess again")
    elif guess > secretNumber:
      print("Too high.")
      print("Guess again")
    else:
      break #This condition is the correct  guess

if guess == secretNumber:
    print('You got it! The answer was ' + str(secretNumber))
else:
    print("You've run out of guesses, you lose.")
