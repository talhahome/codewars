# The new "Avengers" movie has just been released!
# There are a lot of people at the cinema box office standing in a huge line.
# Each of them has a single 100, 50 or 25 dollars bill.
# An "Avengers" ticket costs 25 dollars.
#
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
#
# Can Vasya sell a ticket to each person and give the change if he initially has no money
# and sells the tickets strictly in the order people follow in the line?
#
# Return YES, if Vasya can sell a ticket to each person and give the change
# with the bills he has at hand at that moment.
# Otherwise return NO.
#
# Examples:
# tickets([25, 25, 50]) # => YES
# tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
# tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change
# (you can't make two bills of 25 from one of 50)

def tickets(queue):
    cash = [queue[0]]
    for i in queue[1:]:
        if i == 100:
            if 25 in cash and 50 in cash:
                cash.remove(25)
                cash.remove(50)
                cash.append(100)
            elif cash.count(25) == 3:
                cash.remove(25)
                cash.remove(25)
                cash.remove(25)
                cash.append(100)
            else:
                print("NO")
                return "NO"
        elif i == 50:
            if 25 in cash:
                cash.remove(25)
                cash.append(50)
            else:
                print("NO")
                return "NO"
        elif i == 25:
            cash.append(i)
    print("YES")
    return "YES"

tickets([25, 25, 25, 25, 50, 100, 50])
#tickets([25, 25, 50, 50, 100])
