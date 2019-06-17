# You know what divisors of a number are. The divisors of a positive integer n
# are said to be proper when you consider only the divisors other than n itself.
# In the following description, divisors will mean proper divisors.
# For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.
#
# Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that
# the sum of the proper divisors of each number is one more than the other number:
#
# (n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1
#
# For example 48 & 75 is such a pair:
# Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
# Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
#
# Task
# Given two positive integers start and limit, the function buddy(start, limit) should return
# the first pair (n m) of buddy pairs such that n (positive integer) is between
# start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n
#
# If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil
#
# Examples
# (depending on the languages)
#
# buddy(10, 50) returns [48, 75]
# buddy(48, 50) returns [48, 75]
# or
# buddy(10, 50) returns "(48 75)"
# buddy(48, 50) returns "(48 75)"

from functools import reduce
def buddy(start, limit):
    for i in range(start, limit+1):
        dev = sorted(factors(i))[:-1]
        bud = sum(dev) - 1
        if bud > i:
            bud_dev = sorted(factors(bud))[:-1]
            if sum(bud_dev) - 1 == i:
                print([i, bud])
                return [i, bud]
    print("Nothing")
    return "Nothing"

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#buddy(10, 50)
#buddy(57345, 90061)
# Ans: [62744, 75495]
buddy(1071625, 1103735)
# Ans: [1081184, 1331967]

