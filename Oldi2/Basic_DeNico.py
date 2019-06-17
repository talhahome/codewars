# Write a function deNico/de_nico() that accepts two parameters:
#
# key/$key - string consists of unique letters and digits
# message/$message - string with encoded message
# and decodes the message using the key.
#
# First create a numeric key basing on the provided key by assigning each letter position in
# which it is located after setting the letters from key in an alphabetical order.
#
# For example, for the key crazy we will get 23154 because of acryz (sorted letters from the key).
# Let's decode cseerntiofarmit on using our crazy key.
#
# 1 2 3 4 5
# ---------
# c s e e r
# n t i o f
# a r m i t
#   o n
# After using the key:
#
# 2 3 1 5 4
# ---------
# s e c r e
# t i n f o
# r m a t i
# o n
#
# Notes
# The message is never shorter than the key.
# Don't forget to remove trailing whitespace after decoding the message
#
# Examples
# deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
# deNico("abc", "abcd") => "abcd"
# deNico("ba", "2143658709") => "1234567890"
# deNico("key", "eky") => "key"

import math
def de_nico(key, message):
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
            if e < len(w):
                d.append(w[e])
                e = e + 1
            else:
                break
        # Rearrange "d" according to "z".
        y = []
        for i in range(len(z)):
            if len(d) < len(z):
                if z[i] < len(d):
                    y.append(d[z[i]])
            else:
                y.append(d[z[i]])
        c = c + ''.join(y)
    print(c.rstrip())
    return c.rstrip()

de_nico("crazy", "cseerntiofarmit on  ")
# ANS: "secretinformation"
