"""
Lucky Unicorn Pre-Assessment - V3
Created By: Terry Zhen
"""


# Yes no function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If the user picked yes then start the game
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If the user picked no show instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # If the user enters anything else display error and ask again
        else:
         print("<error> Please Enter y/n")


# Main Routine
question = yes_no("Have you played before? ")
print(f"You have entered '{question}'")
