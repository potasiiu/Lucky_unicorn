"""
Lucky Unicorn Pre-Assessment - V1
Created By: Terry Zhen
"""

# Ask the user if they have played before
show_instructions = input("Have you played before? ")

# If the user picked yes then start the game
if show_instructions == "yes":
    print("Game Start")

# If the user picked no show instructions
elif show_instructions == "no":
    print("Display Instructions")

# If the user enters anything else display error and ask again
else:
    print("<error> Please Enter y/n")