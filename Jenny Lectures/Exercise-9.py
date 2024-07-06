#### pizza order program ####
# small pizza = 100
# medium pizza = 200
# large pizza = 300
#
# pepperoni for small pizza = 30
# pepperoni for medium or large pizza = 50
#
# extra cheese for any size pizza = 20

size = input("Please enter size of pizza (S/M/L): ")

bill = 0

if size == 's' or size == 'S':
    bill += 100
elif size == 'm' or size == 'M':
    bill += 200
else:
    bill += 300

pepperoni = input("Do you want pepperoni (Y/N): ")
if pepperoni == 'y' or pepperoni == 'Y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill += 50

cheese = input("Do you want extra cheese (Y/N): ")
if cheese == 'y' or cheese == 'Y':
        bill += 20

print("The final bill amount is: ", bill)