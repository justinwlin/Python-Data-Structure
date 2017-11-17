'''
September 13, 2017
Implementation of Prime Number

Definition:
let num >= 2 be an integer. We say that num is prime, if its only divisors are 1 and num.

ex.
13 is prime; 12 is not prime

Definition: Let >= 2 be an integer, and let d and k be two divisors of num. WE say that k and d
are complementary divisors of num, if d * k = num

Examples
4 and 25 are complementary divisors of 100

5 and 20 are complementary divisors of 100
'''

def isprime(num):
    countDividers = 0
    upperRange = int(num / 2) + 1
    for curr in range(1, upperRange):
        if num % curr == 0:
            countDividers += 1
        if countDividers == 2:
            return True
        else:
            return False
