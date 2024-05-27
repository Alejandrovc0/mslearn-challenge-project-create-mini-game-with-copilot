# Write a game of rock, paper, scissors. 
# The game should randomly select rock, paper, or scissors.
# The game should prompt the user to select rock, paper, or scissors.
# The game should determine the winner.
# The game should let the user know who won.
# The game should ask the user if they want to play again.
# The game should keep track of the user's wins and losses.
# The user input would be converted to lowercase to avoid case sensitivity
# The game should inform the user if the input is invalid

import random

print("Welcome to Rock, Paper, Scissors game!")
user_wins = 0
comp_wins = 0

while True:
    # Get user's choice
    user_choice = input("Enter rock, paper or scissors: ").lower()

    # Check for invalid input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please enter rock, paper or scissors.")
        continue

    # Get computer's choice
    choices = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(choices)

    print(f"Computer's choice: {comp_choice}")

    # Determine the winner
    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'paper' and comp_choice == 'rock') or (user_choice == 'scissors' and comp_choice == 'paper'):
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        comp_wins += 1

    print(f"User wins: {user_wins}, Computer wins: {comp_wins}")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

