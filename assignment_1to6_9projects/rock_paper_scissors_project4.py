import random

choices = ["rock", "paper", "scissors"]
# Convert each choice to lowercase
choices = [choice.lower() for choice in choices]
#player choice
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#computer_choice
computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")

#winner
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("Computer wins!")