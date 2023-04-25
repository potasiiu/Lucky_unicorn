"""
Lucky Unicorn Pre-Assessment
base component
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


# function that displays instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game will go here")
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not valid input\n" \
            "Please enter a number between {} and {}\n".format(low,high)

    # Keep asking until a valid amount is entered
    while True:
        try:
            # Ask for amount
            response = int(input(question))

            # Check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()
else:
    print("program continues")