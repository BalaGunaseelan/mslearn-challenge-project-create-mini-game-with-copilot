import random

def play_game():
    global player_score, computer_score  # Declare the variables as global if they are used outside this function
    if 'player_score' not in globals():
        player_score = 0
    if 'computer_score' not in globals():
        computer_score = 0

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
 

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
        player_score += 1
        computer_score += 1
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        player_score += 2
    else:
        print("Computer wins!")
        computer_score += 2

while True:
    play_game()
    print("Player score:", player_score)
    print("Computer score:", computer_score)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "y":
        break