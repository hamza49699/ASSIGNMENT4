import random
def guess_the_number():
  number = random.randint(1, 100)
  attempts = 8
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  print("You have 8 attempts to guess the number.")
  while attempts > 0:
    try:
        guess = int(input("Take a guess: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if guess == number:
      print("Congratulations! You guessed the number correctly!")
      return
    elif guess < number:
      print("Too low! Try again.")
    else:
      print("Too high! Try again.")
    attempts -= 1
    print(f"You have {attempts} attempts left.")

  print(f"Sorry, you've run out of attempts. The number was {number}.")
guess_the_number()