import random
import string

def generate_password(length):
    """
    Generates a random password with the given length.
    The password includes uppercase, lowercase, digits, and special characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation  # All possible characters
    password = ''.join(random.choice(characters) for _ in range(length))  # Generate password
    return password

# Get user input for password length
password_length = int(input("Enter the desired password length: "))

# Generate and display the password
password = generate_password(password_length)
print("Your generated password is:", password)