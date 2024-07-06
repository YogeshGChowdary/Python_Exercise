## Select a random name from a list of names and the person selected
# will have to pay for everybody's food bill ###
# This program done using 'choice' keyword.. refer next exercise-12.1 for different method
import random

names = input('enter names of your friends separated by commas: ')

sponser = names.split(',')
bill_payer = random.choice(sponser)

print('sponser for todays bill is:', bill_payer)

