# Import random
import random

# define colors as variables
white = 'white'
gray = 'gray'
black = 'black'
red = 'red'
orange = 'orange'
yellow = 'yellow'
green = 'green'
blue = 'blue'
purple = 'purple'

# make a list of available colors
color_choices = [red, orange, yellow, green, blue, purple]

# create a preliminary color sequence to be appended
color_sequence = [white, white, white, white]

# function to generate and return a random sequence of four colors.
def generate_sequence():
    for i in range(len(color_sequence)):
        color_sequence[i] = random.choice(color_choices)
    print(color_sequence)
    return color_sequence

###### This is hard code, needs to be changed once further code is written.
user_guess = [red, orange, yellow, green]
######

# function to check the accuracy of the user guess.
def check_guess():
    for i in range(len(user_guess)):
        if user_guess[i] == color_sequence[i]:
            indicator_colors[i] = green
        else:
            if user_guess[i] in color_sequence:
                indicator_colors[i] = yellow
            else:
                indicator_colors[i] = red
    return indicator_colors

# call the functions.
generate_sequence()
check_guess()
