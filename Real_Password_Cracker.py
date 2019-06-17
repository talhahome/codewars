# Story
# You are a h4ck3r n00b: you "acquired" a bunch of password hashes, and you want to decypher them.
# Based on the length, you already guessed that they must be SHA-1 hashes.
# You also know that these are weak passwords: maximum 5 characters long
# and use only lowercase letters (a-z), no other characters.
#
# Notes:
# pre-generating the full hash table is not advised, due to the time-limit on the CW platform
# there will be only a few tests for 5-letter words (hint: start from the beginnig of the alphabet)

import hashlib
from itertools import permutations
def password_cracker(hash):
    charSet = 'abcdefghijklmnopqrstuvwxyz'
    m = hashlib.sha1()
    for i in permutations(charSet, 5):
        message = ''.join(i)
        print(message)
        m.update(message.encode('utf-8'))
        sha1 = m.hexdigest()
        print(sha1)
        if sha1 == hash:
            print(message)
            return message

password_cracker("e6fb06210fafc02fd7479ddbed2d042cc3a5155e")
# Ans: "code"
# password_cracker("03de6c570bfe24bfc328ccd7ca46b76eadaf4334")
# Ans: "abcde"
# password_cracker("da23614e02469a0d7c7bd1bdab5c9c474b1904dc")
# Ans: "ab"

# NOT SOLVED !!! ###
# Try find a out a better logic (Time efficient).
# Hash is not always accurate.
# Make length variable and use as permutation argument.
