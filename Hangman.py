import random
from WordsForHangman import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(["a", "b", "cd"]) --> "a b cd"
        print("You have",lives,"Lives left, These are the letters you have used: ", " ".join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        used_letter = input("Guess a letter: ").upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)

            else:
                lives = lives - 1 # takes away a life if wrong
                print("Wrong letter")

        elif used_letter in used_letters:
            print("Already guessed this.")

        else:
            print("What are you doing? Letters please")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You are dead, not sorry. This was the word", word)
    else:
        print("You got it",word,",...you live this time...")

hangman()