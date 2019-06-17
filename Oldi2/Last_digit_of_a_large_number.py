# Define a function that takes in two numbers a and b and returns the last decimal digit of a^b.
# Note that a and b may be very large!
#
# For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969.
# The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.
#
# The inputs to your function will always be non-negative integers.
#
# Examples
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6

def last_digit(n1, n2):
    if n2 == 0:
        return 1
    a = n1 % 10
    if n2 % 4 == 0:
        exp = 4
    else:
        exp = n2 % 4
    ldigit = pow(a, exp)
    print(ldigit % 10)
    return ldigit % 10

last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651)
# Ans: 7
