# Sum of even numbers from 1 to 100 including 1 and 100

#Method-1
sum = 0
for i in range (2,101,2):  #taken step 2, so only even no. are considered
    sum += i
print('sum of even no. 1 to 100 is: ', sum)

#Method-2
sum = 0
for i in range (1,101):
    if i%2 ==0:
        sum += i
print('sum of even no. 1 to 100 is: ', sum)