# How to find maximum number from a list of numbers

numbers = input('Enter list of numbers: ')
numbers_list = numbers.split(',')

count = 0
for num in numbers_list:
    count += 1

for i in range(count):
    numbers_list[i] = int(numbers_list[i])

max_num = numbers_list[0]  # assume number at index 0 is max num
for number in numbers_list:
    if number > max_num:
        max_num = number
print('Maximum number is ', max_num)