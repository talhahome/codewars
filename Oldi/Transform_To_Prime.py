# Task :
# Given a List [] of n integers , find minimum mumber to be inserted in a list,
# so that sum of all elements of list should equal the closest prime number .
#
# Notes
# List size is at least 2 .
# List's numbers will only positives (n > 0) .
# Repeatition of numbers in the list could occur .
# The newer list's sum should equal the closest prime number .
#
# Input >> Output Examples
# 1- minimumNumber ({3,1,2}) ==> return (1)
# Explanation:
# Since , the sum of the list's elements equal to (6) ,
# the minimum number to be inserted to transform the sum to prime number is (1) ,
# which will make the sum of the List equal the closest prime number (7) .
#
# 2-  minimumNumber ({2,12,8,4,6}) ==> return (5)
# Explanation:
# Since , the sum of the list's elements equal to (32) ,
# the minimum number to be inserted to transform the sum to prime number is (5) ,
# which will make the sum of the List equal the closest prime number (37) .
#
# 3- minimumNumber ({50,39,49,6,17,28}) ==> return (2)
# Explanation:
# Since , the sum of the list's elements equal to (189) ,
# the minimum number to be inserted to transform the sum to prime number is (2) ,
# which will make the sum of the List equal the closest prime number (191) .

def minimum_number(numbers):
    total = sum(numbers)
    if is_prime(total):
        print(0)
        return 0
    else:
        i = total
        while True:
            if is_prime(i):
                i = i - total
                print(i)
                return i
            else:
                i += 1

def is_prime(x):
    if x >= 2:
        for y in range(2,x):
            if not (x % y):
                return False
    else:
        return False
    return True

#minimum_number([50, 39, 49, 6, 17, 28]) # Ans 2

minimum_number([2,12,8,4,6])
