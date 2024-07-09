## calculate paint area ##
# 1can = 7sq.mtr =>  no. of cans = ((height x width)/coverage)
# use "ceil" keyword to round values to next integer => 1.4 round to 2, 1.7 round to 2
# import math module -> math.ceil(4.2) -> 5.. ceiling of 4.2 is 5
# math.ceil(-3.7) -> -3.. ceiling of -3.7 is -3

import math
def paint_calculation(height,width,cover):
    area = height * width
    no_of_cans = math.ceil(area / cover)
    print(f'You will need {no_of_cans} cans of paint.')


h = int(input("Enter the height of wall in meters:\n"))
w = int(input('Enter the width of wall in meters:\n'))
coverage = 7

paint_calculation(width=w, height=h, cover=coverage)

