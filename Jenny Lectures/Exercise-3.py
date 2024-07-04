# Add digits of given number

num = (input('provide number to add digits: '))

# num = int(input('provide number to add digits: ')) --> gives error
# num variable is an integer, and you cannot iterate over an integer directly

sum_of_digits = 0

for i in num:
    sum_of_digits += int(i)

print(sum_of_digits)