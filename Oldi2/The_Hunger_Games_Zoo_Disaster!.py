# Story
# A freak power outage at the zoo has caused all of the electric cage doors to malfunction and swing open...
# All the animals are out and some of them are eating each other!
# It's a Zoo Disaster!
#
# Here is a list of zoo animals, and what they can eat
# antelope eats grass
# big-fish eats little-fish
# bug eats leaves
# bear eats big-fish
# bear eats bug
# bear eats chicken
# bear eats cow
# bear eats leaves
# bear eats sheep
# chicken eats bug
# cow eats grass
# fox eats chicken
# fox eats sheep
# giraffe eats leaves
# lion eats antelope
# lion eats cow
# panda eats leaves
# sheep eats grass
#
# INPUT
# A comma-separated string representing all the things at the zoo
# TASK
# Figure out who eats who until no more eating is possible.
# OUTPUT
# A list of strings (refer to the example below) where:
# The first element is the initial zoo (same as INPUT)
# The last element is a comma-separated string of what the zoo looks like when all the eating has finished
# All other elements (2nd to last-1) are of the form X eats Y describing what happened
#
# Notes
# Animals can only eat things beside them
#
# Animals always eat to their LEFT before eating to their RIGHT
#
# Always the LEFTMOST animal capable of eating will eat before any others
#
# Any other things you may find at the zoo (which are not listed above) do not eat anything and are not edible
#
# Example
# INPUT
# "fox,bug,chicken,grass,sheep"
# 1	fox can't eat bug
# "fox,bug,chicken,grass,sheep"
# 2	bug can't eat anything
# "fox,bug,chicken,grass,sheep"
# 3	chicken eats bug
# "fox,chicken,grass,sheep"
# 4	fox eats chicken
# "fox,grass,sheep"
# 5	fox can't eat grass
# "fox,grass,sheep"
# 6	grass can't eat anything
# "fox,grass,sheep"
# 7	sheep eats grass
# "fox,sheep"
# 8	fox eats sheep
# "fox"
#
# OUTPUT
# ["fox,bug,chicken,grass,sheep", "chicken eats bug", "fox eats chicken", "sheep eats grass", "fox eats sheep", "fox"]

def who_eats_who(zoo):
    # Make a list of the animals and things.
    a = zoo.split(',')
    # Make a dictionary of zoo animals, and what they can eat.
    animals = {'antelope': ['grass'],
               'big-fish': ['little-fish'],
               'bug': ['leaves'],
               'bear': ['big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'],
               'chicken': ['bug'],
               'cow': ['grass'],
               'fox': ['chicken', 'sheep'],
               'giraffe': ['leaves'],
               'lion': ['antelope', 'cow'],
               'panda': ['leaves'],
               'sheep': ['grass']}
    b = a[:]
    z = [zoo]
    # Run the loop till the list contain only one animal.
    while len(b) > 1:
        # Check every animals/things until something is eaten.
        for i in range(len(a)):
            # For the middle animals/things of the list. Check previous and next items.
            if 0 < i < len(a) - 1 and a[i] in animals:
                if a[i - 1] in animals[a[i]]:
                    del b[i - 1]
                    z.append(a[i] + ' eats ' + a[i - 1])
                    break
                elif a[i + 1] in animals[a[i]]:
                    del b[i + 1]
                    z.append(a[i] + ' eats ' + a[i + 1])
                    break
            # For the first animal/thing of the list. Check next item only.
            elif i == 0 and a[i] in animals and a[i + 1] in animals[a[i]]:
                del b[i + 1]
                z.append(a[i] + ' eats ' + a[i + 1])
                break
            # For the last animal/thing of the list. Check previous item only.
            elif i == len(a) - 1 and a[i] in animals and a[i - 1] in animals[a[i]]:
                del b[i - 1]
                z.append(a[i] + ' eats ' + a[i - 1])
                break
        # Reassign the shortened list for next check.
        if len(a) > len(b):
            a = b[:]
        else:
            break
    # Add the last remaining animal to the output.
    y = ','.join(a)
    z.append(y)
    print(z)
    return z

who_eats_who("fox,bug,chicken,grass,sheep,stone")
# Output:
# ["fox,bug,chicken,grass,sheep", "chicken eats bug", "fox eats chicken", "sheep eats grass", "fox eats sheep", "fox"]

# who_eats_who("sheep,cow,little-fish,sheep,bear,panda,banana,giraffe,little-fish,bicycle")
# Output:
# ['sheep,cow,little-fish,sheep,bear,panda,banana,giraffe,little-fish,bicycle', 'bear eats sheep', 'sheep,cow,little-fish,bear,panda,banana,giraffe,little-fish,bicycle']

# Execution Timed Out #
# two uneaten elements will go fot infinite loop.
# Try to solve this.
