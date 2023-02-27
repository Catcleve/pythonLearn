import random
import time
import sys

# Define the characters that will be used for the matrix rain
characters = "01"

# Define the colors that will be used for the matrix rain
colors = ["\033[0;32m", "\033[1;32m", "\033[2;32m"]


# Define a function to clear the screen
def clear_screen():
    # Use ANSI escape sequence to clear screen and move cursor to top left corner
    print("\033[2J\033[H", end="")


# Define a function to create a random line of characters
def create_line():
    # Use random.choices to select 80 characters from characters list with equal probability
    line = "".join(random.choices(characters, k=80))
    # Return the line as a string
    return line


# Define a function to create a matrix rain effect
def matrix_rain():
    # Clear the screen before starting the effect
    clear_screen()
    # Create an empty list to store 40 lines of characters
    lines = []
    # Loop 40 times to fill the list with random lines of characters
    for i in range(40):
        lines.append(create_line())

    # Loop indefinitely until user presses Ctrl+C to exit
    while True:
        try:
            # Print each line with a random color from colors list and reset color at the end of each line
            for line in lines:
                print(random.choice(colors) + line + "\033[0m")
            # Wait for 0.1 seconds before updating the screen
            time.sleep(0.1)
            # Clear the screen before printing next frame of effect
            clear_screen()
            # Update each line by shifting it one character to the right and adding a new random character at the
            # beginning
            for i in range(40):
                lines[i] = create_line()[0] + lines[i][:-1]
        except KeyboardInterrupt:
            # If user presses Ctrl+C, exit the loop and program gracefully 
            break


# Call the matrix_rain function to start the effect
matrix_rain()
