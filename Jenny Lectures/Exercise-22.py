# prime checker

import math
def prime_checker(num):
    is_prime = True
    if num == 1:
        is_prime = False
    for i in range (2,math.ceil(num/2)+1): # to check prime, range half of given num is sufficient to check
        if num%i == 0:
            is_prime=False
    if is_prime == True:
        print('It is a prime number')
    else:
        print('Not a prime number')

num = int(input('please enter no. to check:\n'))
prime_checker(num)
