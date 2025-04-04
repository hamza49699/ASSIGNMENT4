def sum(a, b, c):
    # Function to sum three values
    return a + b + c


def printBoard(xState, zState):
    # Function to display the Tic-Tac-Toe board
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    
    # Print the Tic-Tac-Toe board
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def checkWin(xState, zState):
    # Function to check if any player has won
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O Won the match")
            return 0
    return -1  # No winner yet


if __name__ == "__main__":
    # Initialize board states
    xState = [0] * 9  # Track positions occupied by 'X'
    zState = [0] * 9  # Track positions occupied by 'O'
    turn = 1  # 1 for X's turn, 0 for O's turn
    
    print("Welcome to Tic Tac Toe")
    
    while True:
        printBoard(xState, zState)  # Display board
        
        if turn == 1:
            print("X's Chance")
        else:
            print("O's Chance")
        
        # Get user input and update state
        value = int(input("Please enter a value (0-8): "))
        if xState[value] or zState[value]:
            print("Position already taken. Try again!")
            continue
        
        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1
        
        # Check if there is a winner
        cwin = checkWin(xState, zState)
        if cwin != -1:
            printBoard(xState, zState)
            print("Match over")
            break
        
        turn = 1 - turn  # Switch turn
