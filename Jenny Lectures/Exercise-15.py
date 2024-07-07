# How to find maximum number from a list of numbers
# refer Exercise-15.1 for different approach, dont use "max" keyword

num = input('Enter no. to find max no.: ')
num_list = num.split(',')

int_num = (int(i) for i in num_list)

max_value = max(int_num)
print('Max value in given no.s is: ', max_value)