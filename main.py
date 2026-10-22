# import functions!
from wordle_functions import (
    choose_word,
    get_guess,
    evaluate_guess,
    display_guess,
    has_won,
)

MAX_ATTEMPTS = 6

print("Welcome to Mystery Wordle!")

play_again = "yes"

# use functions to set up game
while play_again == "yes":
    secret_word = choose_word()
    previous_guesses = []
    solved = False

    #give feedback instructions according to the rules
    print("Guess the five-letter word.")
    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter is not in the word")

    # give the player up to six attempts
    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"Attempt {attempt} of {MAX_ATTEMPTS}")

        # get a valid guess and save it
        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, secret_word)
        # show the guess with its feedback
        display_guess(guess, feedback)

        # end the round early if the player won
        if has_won(feedback):
            print("Congratulations! You solved the puzzle.")
            solved = True
            break

    if not solved:
        print(f"Out of attempts! The secret word was {secret_word}.")

    play_again = input("Would you like to play again? ").strip().lower()

print("Thanks for playing!")