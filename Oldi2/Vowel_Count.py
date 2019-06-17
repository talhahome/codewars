# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, and u as vowels for this Kata.
#
# The input string will only consist of lower case letters and/or spaces.

def getCount(inputStr):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in inputStr:
        if i in vowels:
            num_vowels = num_vowels + 1
    return num_vowels

print(getCount("abracadabra"))
# Ans: 5

### Clever Solutions ###

# def getCount(inputStr):
#    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# def getCount(s):
#     return sum(c in 'aeiou' for c in s)
