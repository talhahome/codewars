# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
# N! = 1 * 2 * 3 * ... * N
#
# Examples
# zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
#
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

def zeros(n):
    a = int(n/5)
    if a < 5:
        print(int(a))
        return int(a)
    z = a
    while int(a/5) >= 1:
        z = z + int(a/5)
        a = int(a/5)
    print(z)
    return z

zeros(10000)
