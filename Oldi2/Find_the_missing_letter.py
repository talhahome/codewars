# Write a method that takes an array of consecutive (increasing) letters as input
# and that returns the missing letter in the array.
#
# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.
#
# Example:
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

def find_missing_letter(z):
    return [chr(i) for i in range(ord(z[0]), ord(z[-1])) if chr(i) not in z][0]

print(find_missing_letter(['a','b','c','d','f']))
