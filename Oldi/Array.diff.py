# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    for i in range(len(b)):
        if b[i] in a:
            c = []
            for j in range(len(a)):
                if b[i] != a[j]:
                    c.append(a[j])
            a = c
        else:
            continue
    print(a)
    return a

a = [1,2,2]
b = [2]
array_diff(a, b)