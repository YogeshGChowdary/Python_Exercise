# Guess the number

import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number,answer,attempts):
    if guessed_number < answer:
        print("Your guess is too low")
        return attempts-1
    else:
        print(f"Your guess is right... The answer was {answer}")

def game():
    print("let me think of a number between 1 to 50.")
    answer = random.randint(1,50)
    print(answer)
    level = input('choose level of difficulty.. enter easy or hard: ')
    attempts = set_difficulty(level)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
        print("You have entered wrong difficulty level... Play again!!!")
        return  #With return: If the condition is met, the function stops executing immediately
                # after printing the message. This is useful to prevent further code from running when
                # an invalid difficulty level is detected.
                # Without return: If you remove the return statement, the function will continue
                # executing any subsequent code after the print statement, even if the user entered
                # an invalid difficulty level. This might lead to unintended behavior or errors if the
                # subsequent code assumes a valid difficulty level.

    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Guess the number: "))
        attempts = check_answer(guessed_number,answer,attempts)
        if attempts == 0:
            print('You are out of guesses... You lose!')
            return
        elif guessed_number != answer:
            print("Guess again")

game()