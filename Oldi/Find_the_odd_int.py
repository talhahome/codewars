# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    a = list(set(seq))
    for i in range(len(a)):
        b = seq.count(a[i])
        if b % 2 != 0:
            print(a[i])
            return a[i]
    return None

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
find_it(seq)
