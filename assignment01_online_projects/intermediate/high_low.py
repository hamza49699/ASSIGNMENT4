import random

NUM_ROUNDS = 5  # Number of rounds to play

def get_valid_input():
    """Ensures the user enters a valid guess: 'higher' or 'lower'."""
    while True:
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if guess in ["higher", "lower"]:
            return guess
        print("Please enter either 'higher' or 'lower'.")

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # Player's score
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Show the user their number (but not the computer's)
        print(f"Your number is {user_number}")
        
        # Get user's guess
        user_guess = get_valid_input()
        
        # Determine the outcome
        if (user_guess == "higher" and user_number > computer_number) or \
           (user_guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increase score on correct guess
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Display the current score
        print(f"Your score is now {score}\n")
    
    # Final message based on performance
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
if __name__ == "__main__":
    main()
