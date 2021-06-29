import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Choose an option: 0 for Rock, 1 for Paper or 2 for scissors\n"))

if user_choice >= 3 or user_choice < 0:
  print("You type an invalid number, You lose!")
else:
  print(game_images[user_choice])

  pc_choice = random.randint(0, 2)
  print("computer chose: ")
  print(game_images[pc_choice])

  if user_choice == 0 and pc_choice == 2:
    print("You Win!")
  elif pc_choice == 0 and user_choice == 2:
    print("You Lose!")
  elif pc_choice > user_choice:
    print("you lose!")
  elif user_choice >pc_choice:
    print("You win!")
  elif pc_choice == user_choice:
    print("It's a draw")


