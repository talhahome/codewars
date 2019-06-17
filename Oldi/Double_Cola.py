# Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine;
# there are no other people in the queue.
# The first one in the queue (Sheldon) buys a can, drinks it and doubles!
# The resulting two Sheldons go to the end of the queue.
# Then the next in the queue (Leonard) buys a can,
# drinks it and gets to the end of the queue as two Leonards, and so on.
#
# For example, Penny drinks the third can of cola and the queue will look like this:
# Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
#
# Write a program that will return the name of the person who will drink the n-th cola.
#
# Input
# The input data consist of an array which contains at least 1 name, and single integer n.
# 1  ≤  n  ≤  1000000000
#
# Output / Examples
# Return the single line — the name of the person who drinks the n-th can of cola.
# The cans are numbered starting from 1.
# whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
# whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
# whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"

import math
def whoIsNext(names, r):
    totalvalue = 0
    i = 0
    notified = False
    lengths = len(names)
    if r <= len(names):
        return names[r - 1]
    while totalvalue < r and not notified:
        totalvalue += lengths * (2 ** i)
        i += 1
        if totalvalue + lengths * (2 ** i) >= r:
            notified = True
    numInPlace = 2 ** i
    rest = r - totalvalue
    position = math.ceil(rest / numInPlace)
    print(names[position - 1])
    return names[position - 1]

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
r = 7230702951
whoIsNext(names,r)

### Easiest Solution possible ###
# def whoIsNext(names, r):
#    while r > 5:
#        r = (r - 4) / 2
#    return names[int(r) - 1]