import time

def countdown_timer(seconds):
    """
    This function takes the number of seconds as input and starts a countdown timer.
    It displays the remaining time in MM:SS format and updates every second.
    """
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert total seconds to minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Format time as MM:SS
        print(timer, end="\r")  # Print on the same line to update the timer display
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease time by 1 second

    print("00:00 \nTime's up!")  # Notify when the countdown ends

# User input for the timer
total_seconds = int(input("Enter the time in seconds: "))
countdown_timer(total_seconds)  # Start the countdown
