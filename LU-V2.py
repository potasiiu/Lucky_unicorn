"""
Lucky Unicorn Pre-Assessment - V2
Created By: Terry Zhen
"""

# Ask the user if they have played before
show_instructions = input("Have you played before? ").lower()

# Show the user what they inputted
print(f"You have entered '{show_instructions}'")

# If the user picked yes then start the game
if show_instructions == "yes" or show_instructions == "y":
    print("Game Start")

# If the user picked no show instructions
elif show_instructions == "no" or show_instructions == "n":
    print("Display Instructions")

# If the user enters anything else display error and ask again
else:
    print("<error> Please Enter y/n")

