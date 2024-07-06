# #### Rock Paper Scissors ####
# #Rules: Rock wins against scissors              ## 0 for rock
# scissors win against paper                      ## 1 for paper
# paper wins against rock                         ## 2 for scissors

# user choice(0,1,2)          computer choice(0,1,2)
# 		0							0                            Draw
# 		0                           1           				 computer win
# 		0                           2							 user win
# 		1                           0                            user win
# 		1                           1     						 Draw
# 		1                           2							 computer win
# 		2                           0 							 computer win
# 		2                           1                            user win
# 		2                           2                            Draw

#order of condition statements is important, mention user=0,computer=2 and computer=0,user=2 condition
# before other conditions so result will be correct
import random

user_choice = int(input("enter your choice of no. "))
print("user choice is: ", user_choice)
computer_choice = random.randint(0,2)
print('computer choice is: ', computer_choice)

if user_choice >=3 or user_choice < 0:
    print("You entered invalid number, You Lose")
else:
    if user_choice == computer_choice:
        print('Its Draw')
    elif user_choice == 0 and computer_choice == 2:
        print('You win')
    elif user_choice == 2 and computer_choice == 0:
        print('You Lose')
    elif user_choice > computer_choice:
        print('You win')
    elif user_choice < computer_choice:
        print('You Lose')
