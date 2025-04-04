import random  # Import the random module to select a random word

# List of words to choose from
words = ['enum', 'python', 'collab', 'vscode', 'game']

# Select a random word from the list
word = random.choice(words)

# List to store guessed letters
guessed_letters = []

# Maximum number of incorrect attempts allowed
attempts = 6

# Display a welcome message
print("Welcome to Hangman Game!")

# Display underscores representing the hidden word
print(" ".join(["_" for _ in word]))

# Main game loop
while attempts > 0:
    # Ask the player to input a letter
    guess = input("\nGuess a letter: ").lower()

    # Validate input: must be a single alphabetic character
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue  # Ask for input again if invalid

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print("Correct guess!")  # Inform the player of a correct guess
    else:
        print("Incorrect guess!")
        attempts -= 1  # Decrease remaining attempts for incorrect guesses
        print(f"You have {attempts} attempts left.")

    # Display the word with guessed letters revealed
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    # Check if the player has guessed all the letters correctly
    if "_" not in displayed_word:
        print("Congratulations! You won!")
        break  # Exit the loop if the player wins

# If the player runs out of attempts, they lose
if attempts == 0:
    print(f"Sorry, you lost! The word was '{word}'.")
