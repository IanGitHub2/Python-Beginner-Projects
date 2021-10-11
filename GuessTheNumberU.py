import random

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. To low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"You got it right it was {random_number}. Now that will be $20 buck.")

guess(10)