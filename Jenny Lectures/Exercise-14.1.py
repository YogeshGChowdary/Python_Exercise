#### calculate average height from a list of heights
# dont use keywords 'sum','length' and take input from user for calculation
# use "for loop' for writing program

heights = input('enter all heights separated by space: ')
height_list = heights.split(",")

count = 0
for i in height_list:
    count += 1

for i in range(count):
    height_list[i] = int(height_list[i])

total = 0
for j in height_list:
    total += j

avg = total / count

print('Avg of given values is: ', round(avg,1))