import random

# Words are uppercase so comparisons are consistent.
word_list = ["PLANT", "AUDIO", "CRANE", "SLATE", "BRICK", "POUND", "MOUSE", "CRABS"]

def choose_word():
    #choose and return a secret word from the list
    return random.choice(word_list)

def get_guess(previous_guesses):
    #Ask for a five-letter guess that has not already been used
    while True:
        guess = input("Enter a five-letter word: ").strip().upper()

        if len(guess) != 5 or not guess.isalpha():
            print("Please enter exactly five letters.")
        elif guess in previous_guesses:
            print("You already guessed that word. Try another.")
        else:
            return guess

def evaluate_guess(guess, secret_word):
    # Build a list of feedback, one symbol per letter in the guess
    feedback = []

    for index in range(5):
        # G: right letter in the right position
        if guess[index] == secret_word[index]:
            feedback.append("G")
        # Y: letter is in the word but in a different position
        elif guess[index] in secret_word:
            feedback.append("Y")
        # -: letter is not in the word at all
        else:
            feedback.append("-")

    return feedback

def display_guess(guess, feedback):
    #Display the guess and its feedback
    print("Guess:    ", " ".join(guess))
    print("Feedback: ", " ".join(feedback))


def has_won(feedback):
    #Return True if every letter is correct and in position
    return feedback == ["G", "G", "G", "G", "G"]
