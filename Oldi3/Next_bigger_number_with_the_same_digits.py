# You have to create a function that takes a positive integer number
#
# and returns the next bigger number formed by the same digits:
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
#
# If no bigger number can be composed using those digits, return -1:
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1

def next_bigger(input):
    input = list(map(int, list(str(input))))
    for i in range(1, len(input)):
        # Elements from Right elements which are greater then Current element
        y = [*filter(lambda x: x > input[-(i + 1)], input[-(i):])]
        if y != []:
            # Right elements
            z = input[-(i):]
            # Current element
            a = input[-(i + 1)]
            input[-(i + 1)] = min(y)
            z.remove(min(y))
            z.append(a)
            output = input[:-i] + sorted(z)
            print(int(''.join(list(map(str, output)))))
            return int(''.join(list(map(str, output))))
        else:
            continue
    print(-1)
    return -1

#next_bigger(7122795)
#next_bigger(619876)
next_bigger(1234567890)

