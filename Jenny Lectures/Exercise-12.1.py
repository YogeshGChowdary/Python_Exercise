## Select a random name from a list of names and the person selected
# will have to pay for everybody's food bill ###
# This program done using index method

import random

names = input("Enter everybody's name separated by comma:" )
sponser = names.split(',')
length = len(sponser)

random_choice = random.randint(0,length-1)
print('Todays sponser for bill is: ', sponser[random_choice])