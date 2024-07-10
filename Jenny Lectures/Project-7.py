# Guess the number
# refer project-7.1 for more defined program

import random

guessed_number = random.randint(1,51)
print(guessed_number)

print('Guess the number between 1 to 50')
#number = int(input('guess the number: '))
number = 0
while number != guessed_number:
    number = int(input("guess the number: "))
    print('please try again')

print('You guessed correct')
