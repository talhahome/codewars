#################################################
# Find if a string is containing any character other then "(" & ")".
# Function will return True or False.
# import re
# def is_valid(string):
#    s = re.compile(r'[^()]')
#    x = s.search(string)
#    print(not bool(x))
#    return (not bool(x))

#################################################
# Find numeric values in a string.
# Example:
# str = "In 2015, I want to know how much does iPhone 6+ cost?"
# The numbers are 2015, 6
# import re
# def sum_from_string(string):
#    a = re.findall(r'(\d+)', string)
#    a = [int(y) for y in a]
#    return a

#################################################
# Find indexes(j) of the element 'y' in the list 'x'.
# w = [j for j, k in enumerate(x) if k == y]

#################################################
# Remove elements(a) of index(b) from a set of indexes(w).
# x = [a for b, a in enumerate(x) if b not in w]

#################################################
# Check if a number(x) is prime or not.
# Function will return True or False.
# import math
# def is_prime(x):
#    if x >= 2:
#        for y in range(2,int(math.sqrt(x))+1):
#            if not (x % y):
#                return False
#    else:
#        return False
#    return True

#################################################
# Find factorial of n.
# def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)

#################################################
# Perform float arithmetic operations.
#
# Find decimal places of a float (p).
# import decimal
# p = 7.304
# q = decimal.Decimal(str(p))
# r = q.as_tuple().exponent     # return: -4
#
# Arithmetic operation & round up.
# p = p * 10
# p = round(p, abs(r))          # return: 73.04

#################################################
# Create a SHA1 hash from plaintext.
#
# import hashlib
# m = hashlib.sha1()
# message = "ab"
# sha1 = "03de6c570bfe24bfc328ccd7ca46b76eadaf4334"
# m.update(message.encode('utf-8'))
# print(m.hexdigest())

#################################################
# Generate random combination of strings (a - z) with a range of length (1 - 5).
#
# import random
# charSet = 'abcdefghijklmnopqrstuvwxyz'
# minLength = 1
# maxLength = 5
# length = random.randint(minLength, maxLength)
# for _ in range(length):
#     print(''.join(random.choice(charSet)))

#################################################
# Generate all possible combination of strings (a - z) with a fixed length (5).
#
# from itertools import permutations
# charSet = 'abcdefghijklmnopqrstuvwxyz'
# for i in permutations(charSet, 5):
#     print(''.join(i))

#################################################
# Find all proper factors of an integer number.
#
# from functools import reduce
# def factors(n):
#     return set(reduce(list.__add__,
#                 ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
#
# print(sorted(factors(62744)))

#################################################
#

#################################################
#
