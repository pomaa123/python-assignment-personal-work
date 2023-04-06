# first euler problem
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000
'''

total = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        total += i

print(total)

i = 1
while i <= 10:
    print(i)
    i += 1


#### second euler problem ###
'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
 find the sum of the even-valued terms.
'''
first, second = 1, 2

sum = 0
while second <= 4000000:
    if second % 2 == 0:
        # print(second)
        sum += second 
    third = first + second    
    first = second
    second = third
    
print(sum)

  
#third euler problem
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

# print(largest_prime_factor(600851475143))
import math
from math import sqrt

def factor(n):
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    return list


def is_prime(n0):

    if n0 < 2:
        return False 
    for i in range(2, int(sqrt(n0))+1):
        if n0 % i == 0:
            return False    
    return True


def find_prime(n, factor):
    primes = []
    factors = factor(n)
    for num in factors:
        if is_prime(num):
            primes.append(num)
    
    return max(primes)

find_prime(13195, factor)


