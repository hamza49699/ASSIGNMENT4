# Get user input
curr_value = int(input("Enter a number: "))

# Loop to double the value until it reaches or exceeds 100
while curr_value < 100:
    curr_value *= 2  # Double the current value
    print(curr_value, end=" ")  # Print the value on the same line with a space
