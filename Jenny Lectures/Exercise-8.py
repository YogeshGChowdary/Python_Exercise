# check whether given year is leap year or not
# A year is a leap year if:
#     - It is divisible by 4
#     - If it is divisible by 100, it should also be divisible by 400

year = int(input('please enter year to check: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('given year is leap year')
else:
    print('given year is not leap year')


