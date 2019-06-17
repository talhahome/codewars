# Complete the function scramble(str1, str2) that returns true
# if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
# Notes:
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered
# Input strings s1 and s2 are null terminated.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(str1, str2):
    if len(str1) < len(str2):
        return False
    for i in str2:
        if i not in str1:
            return False
        str1 = str1.replace(i, '', 1)
    return True

print(scramble('qzmskjnidkepv', 'uqkubshfpifexpmao'))
# Performance test failed for 80000 characters input.

### Below code is the best solution for this performance check ###
# from collections import Counter
# def scramble(s1, s2):
#     return not(Counter(s2) - Counter(s1))

