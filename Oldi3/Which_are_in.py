# Given two arrays of strings a1 and a2 return
# a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
#
# Example 1:
# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns ["arp", "live", "strong"]
#
# Example 2:
# a1 = ["tarp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns []
#
# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: r must be without duplicates.
# Don't mutate the inputs.

def in_array(a1, a2):
    r = []
    for i in a1:
        x = [i for j in a2 if i in j]
        if x != []:
            r.append(list(set(x))[0])
    return sorted(list(set(r)))

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
