# Given a list lst and a number N,
# create a new list that contains each number of lst at most N times without reordering.
# For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2]
# since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
# Example
#   delete_nth ([1,1,1,1],2) # return [1,1]
#   delete_nth ([20,37,20,21],1) # return [20,37,21]

def delete_nth(order,max_e):
    x = []
    for i in range(len(order)):
        # Find indexes of the element 'order[i]' in the list 'order'
        z = [j for j, y in enumerate(order) if y == order[i]]
        if len(z) <= max_e:
            x.append(order[i])
        else:
            p = [k for k, q in enumerate(x) if q == order[i]]
            if len(p) < max_e:
                x.append(order[i])
            else:
                continue
    return x

delete_nth ([20,37,20,21],1)

