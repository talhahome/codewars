# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
#
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]


def move_zeros(array):
    zeros = [0, 0.0]
    b = []
    for i in array:
        if i in zeros and str(i) != 'False':
            continue
        else:
            b.append(i)
    count = len(array) - len(b)
    print(b + [0]*count)
    return b + [0]*count


move_zeros([false,1,0,1,2,0,1,3,"a"])


# Another approach.
# def move_zeros(array):
#     b = [i for i in array if isinstance(i, bool) or i != 0]
#     count = len(array) - len(b)
#     return b + [0]*count

