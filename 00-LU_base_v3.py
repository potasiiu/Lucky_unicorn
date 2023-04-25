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
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then press <enter> to play. You will get a random token which might"
          "be a horse, a zebra, a donkey, or a unicorn")
    print()
    print("It costs $1 to play each round but, dpending on your prize, you "
          "could win some of your money back. These are the payout amounts:\n"
          "\tUnicorn: $5 (balance increases by $4\n"
          "\tHorse: $0.5 (balance decreases by $0.5\n"
          "\tZebra: $0.5 (balance decreases by $0.5\n"
          "\tDonkey: $0.00 (balance decreases by $1\n")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with "
          "more money than you started with.\n")
    print("*" * 50)
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
        print(formatter(".", f"Round {rounds_played}"))
        number = random.randint(1, 100)  # can only be a donkey

        # adjust balance
        # if the random number is between 1 and 5
        # user gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            balance += 4
            print(formatter("!", "Congratulations, you got a Unicorn"))
            print()

        # if the random number is between 6 adn 36
        # user gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "Oh No, You got a Donkey"))
            print()

        # in all other cases the token must be a horse or a zebra
        # (subtract $0.50 from the balance in either case)
        else:
            # if the number is even, set the token to horse
            if number % 2 == 0:
                balance -= .5
                print(formatter("H", "You got a Horse"))
                print()

            # otherwise, set the token to zebra
            else:
                balance -= .5
                print(formatter("Z", "You got a Zebra"))
                print()

        # output
        print(f"Your balance is now ${balance}")
        if balance < 0:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> to play"
                               "again or 'X' to exit ").lower()
        print()
    return balance

def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()


# ask the user how much they want to play with
starting_balance= num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print(formatter("*", "Goodbye"))