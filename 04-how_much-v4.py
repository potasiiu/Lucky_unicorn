"""
Component 2 (How much) v4
Turns v3 into a function
"""


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
user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")