# Fizz Buzz Problem
# print numbers from 1 to 100,
# for no.s divisible by 3 -> print fizz, divisible by 5 -> buzz, divisible by both 3 and 5 -> fizzbuzz
# order of conditions is important, first consiber condition with max probability like
# first check divisibilty by 3 and 5, then 3 and 5

for i in range(1,101):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
