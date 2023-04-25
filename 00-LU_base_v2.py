"""
Lucky Unicorn Pre-Assessment
base component
Created By: Terry Zhen
"""
import random


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


# Function to generate random token
def generate_token(balance):
    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
        number = random.randint(1, 100)  # can only be a donkey

        # adjust balance
        # if the random number is between 1 and 5
        # user gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4

        # if the random number is between 6 adn 36
        # user gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # in all other cases the token must be a horse or a zebra
        # (subtract $0.50 from the balance in either case)
        else:
            # if the number is even, set the token to zebra
            if number % 2 == 0:
                token = "zebra"
                balance -= .5

            # otherwise, set the token to zebra
            else:
                token = "horse"
                balance -= .5

        # output
        print(f"Round {rounds_played}. Token: {token}, Balance ${balance}")
        if balance < 0:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> to play"
                               "again or 'X' to exit ").lower()
        print()
    return balance


# Main Routine
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()


# ask the user how much they want to play with
starting_balance= num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print("Goodbye")