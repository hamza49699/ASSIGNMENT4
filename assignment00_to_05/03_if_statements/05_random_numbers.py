import random

def print_random_numbers():
    """
    Prints 10 random numbers in the range 1 to 100.
    """
    for _ in range(10):
        print(random.randint(1, 100), end=" ")

print_random_numbers()
