# Write a function nico/nico() that accepts two parameters:
#
# key/$key - string consists of unique letters and digits
# message/$message - string to encode
# and encodes the message using the key.
#
# First create a numeric key basing on a provided key by assigning each letter position in
# which it is located after setting the letters from key in an alphabetical order.
#
# For example, for the key crazy we will get 23154 because of acryz (sorted letters from the key).
# Let's encode secretinformation using our crazy key.
#
# 2 3 1 5 4
# ---------
# s e c r e
# t i n f o
# r m a t i
# o n
# After using the key:
#
# 1 2 3 4 5
# ---------
# c s e e r
# n t i o f
# a r m i t
#   o n
# Notes
# The message is never shorter than the key.
#
# Examples
# nico("crazy", "secretinformation") => "cseerntiofarmit on  "
# nico("abc", "abcd") => "abcd  "
# nico("ba", "1234567890") => "2143658709"
# nico("key", "key") => "eky"
# Check the test cases for more samples.

import math
def nico(key, message):
    # Convert the "key" into numeric key.
    a = list(key)
    b = sorted(a)
    z = []
    for i in range(len(b)):
        z.append(b.index(a[i]))
    # Make a 2 dimensional array with "message" characters.
    w = list(message)
    b = math.ceil(len(message) / len(key))
    c = ''
    e = 0
    for k in range(b):
        d = []
        for l in range(len(key)):
            if e < len(message):
                d.append(w[e])
                e = e + 1
            else:
                d.append(' ')
        # Rearrange "d" according to "z".
        y = []
        for i in range(len(d)):
            y.append(d[z.index(i)])
        c = c + ''.join(y)
    print(c)
    return c

nico("crazy", "secretinformation")
# ANS: "cseerntiofarmit on  "
