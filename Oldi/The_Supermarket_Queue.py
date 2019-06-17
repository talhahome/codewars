# There is a queue for the self-checkout tills at the supermarket.
# Your task is write a function to calculate the total time required for all the customers to check out!
#
# The function has two input variables:
# customers: an array (list in python) of positive integers representing the queue.
# Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# The function should return an integer, the total time required.
#
# There is only ONE queue, and
# The order of the queue NEVER changes, and
# Assume that the front person in the queue (i.e. the first element in the array/list)
# proceeds to a till as soon as it becomes free.
# The diagram on the wiki page I linked to at the bottom of the description may be useful.
#
# So, for example:
# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times
#
# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the
# # queue finish before the 1st person has finished.
#
# queue_time([2,3,10], 2)
# # should return 12
# N.B. You should assume that all the test input will be valid, as specified above.

def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    elif len(customers) == 1:
        return customers[0]
    elif len(customers) <= n:
        return max(customers)
    elif n == 1:
        return sum(customers)
    else:
        x = [p for p in customers[:n]]
        z = []
        q = customers[:]
        for l in range(len(x)):
            q.pop(q.index(x[l]))
        y = min(x)
        z.append(y)
        i = n
        while len(q) >= 1:
            # Find indexes of the element 'y' in the list 'x'
            w = [j for j, k in enumerate(x) if k == y]
            if len(w) <= 1:
                x.pop(x.index(y))
                x[:] = [s - y for s in x]
                x.append(customers[i])
                q.pop(q.index(customers[i]))
                i += 1
            else:
                # Remove elements with lowest value
                x = [a for b, a in enumerate(x) if b not in w]
                x[:] = [s - y for s in x]
                # Add elements from the input array 'customers'
                if len(w) <= len(q):
                    for l in range(len(w)):
                        x.append(customers[i])
                        q.pop(q.index(customers[i]))
                        i += 1
                else:
                    for l in range(len(q)):
                        x.append(customers[i])
                        q.pop(q.index(customers[i]))
                        i += 1
            if len(q) > 0:
                y = min(x)
                z.append(y)
            else:
                z.append(max(x))
    print(sum(z))
    return sum(z)

#queue_time([5,3,4], 1)     # Ans 12
#queue_time([10,2,3,3], 2)  # Ans 10
#queue_time([2,3,10], 2)    # Ans 12

#queue_time([2,2,3,3,4,4], 2)   # Ans 9

queue_time([14, 45, 3, 44, 23, 16, 27, 6, 35, 27, 37, 41, 4, 23], 5)    # Ans 85

### Best Solution ###
#def queue_time(customers, n):
#    l=[0]*n
#    for i in customers:
#        l[l.index(min(l))]+=i
#    return max(l)
