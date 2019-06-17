# Given a random string consisting of numbers, letters, symbols, you need to sum up the numbers in the string.
#
# Note:
# Consecutive integers should be treated as a single number. eg, 2015 should be treated as a single number 2015,
# NOT four numbers
# All the numbers should be treated as positive integer. eg, 11-14 should be treated as two numbers 11
# and 14. Same as 3.14, should be treated as two numbers 3 and 14
# If no number was given in the string, it should return 0
#
# Example:
# str = "In 2015, I want to know how much does iPhone 6+ cost?"
# The numbers are 2015, 6
# Sum is 2021.

import re
def sum_from_string(string):
    a = re.findall(r'(\d+)', string)
    print(a)
    a = [int(y) for y in a]
    print(sum(a))
    return sum(a)

#sum_from_string("In 2015, I want to know how much does iPhone 6+ cost?")    # Ans: 2021
sum_from_string("1+1=2")
