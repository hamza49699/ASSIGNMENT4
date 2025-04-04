import random  # Import the random module to generate random numbers

def computer_guess_the_number():
    """
    A game where the computer tries to guess the number the user is thinking of.
    The user provides feedback to guide the computer's guesses.
    """
    
    print("Welcome to the Computer Guessing Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")

    # Define the range in which the number lies
    low = 1  # Minimum possible number
    high = 100  # Maximum possible number
    attempts = 8  # Maximum number of guesses allowed
    feedback = ''  # Variable to store user feedback

    while attempts > 0:
        # Computer makes a guess within the current range
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")

        # Ask the user for feedback on the guess
        feedback = input("Is my guess too high, too low, or correct? (h/l/c): ").lower()

        # If the guess is correct, the game ends
        if feedback == 'c':
            print("Hooray! I guessed the number correctly!")
            return
        # If the guess is too high, adjust the upper bound
        elif feedback == 'h':
            high = guess - 1
        # If the guess is too low, adjust the lower bound
        elif feedback == 'l':
            low = guess + 1
        # Handle invalid input
        else:
            print("Invalid input. Please enter 'h' for high, 'l' for low, or 'c' for correct.")
            continue  # Skip the rest of the loop and ask again

        # Reduce the number of remaining attempts
        attempts -= 1
        print(f"You have {attempts} attempts left.")

    # If the computer runs out of attempts, the user wins
    print("I couldn't guess your number in time. You win!")

# Call the function to start the game
computer_guess_the_number()
