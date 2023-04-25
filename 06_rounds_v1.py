"""Component 4 - game mechanis and looping v1
Based on 05_token_generator_v4 but hard wired to only allocate donkeys
gives user feedback about number of round and maintains balance.
Test amount set to $5
"""

import random

# Main routine
TEST_AMOUNT = 5
balance = 5

rounds_played = 0
play_again = ""

# Testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1 # keep track of rounds
    number = random.randint(6,36) # can only be a donkey

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
    if balance < 1:
        print("\nSorry but you have run out of money")
        play_again = "x"
    else:
        play_again = input("\nDo you want to play another round?\n<enter> to play"
                           "again or 'X' to exit ").lower()
        print()

print("Thanks for playing")
print(f"You started with ${TEST_AMOUNT:.2f}")
print(f"and leave with ${balance:.2f}")
print("Goodbye")
