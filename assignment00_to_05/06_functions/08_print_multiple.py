def print_multiple(message, repeats):
    """Prints the given message the specified number of times."""
    for _ in range(repeats):
        print(message, end=" ")  # Print on the same line with a space

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

main()
