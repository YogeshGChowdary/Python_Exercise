#### calculate average height from a list of heights
# dont use keywords 'sum','length' and take input from user for calculation
# use "for loop' for writing program
# This program done for understanding, refer Exercise-14.1 for different approach

heights = input('Please enter height value in cms to calculate avg separated by comma: ')
ind_heights = heights.split(',')
total_heights = [int(height) for height in ind_heights]
total_length = (len(ind_heights))
total_sum = sum(total_heights)
avg = (total_sum /total_length )

print('avg height value is: ', avg)
