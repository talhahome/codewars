# A bookseller has lots of books classified in 26 categories labeled A, B, ... Z.
# Each book has a code c of 3, 4, 5 or more capitals letters.
# The 1st letter of a code is the capital letter of the book category.
# In the bookseller's stock list each code c is followed by a space and by a positive integer n (int n >= 0)
# which indicates the quantity of books of this code in stock.
#
# For example an extract of one of the stock lists could be:#
# L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
# or
# L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
# You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :
#   M = {"A", "B", "C", "W"}
# or
#   M = ["A", "B", "C", "W"] or ...
# and your task is to find all the books of L with codes belonging to each category of M
# and to sum their quantity according to each category.
#
# For the lists L and M of example you have to return the string (in Haskell/Clojure a list of pairs):
#   (A : 20) - (B : 114) - (C : 50) - (W : 0)
# where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum
# corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W'
# since there are no code beginning with W.
# If L or M are empty return string is "" (Clojure should return an empty array instead).
#
# Note:
# In the result codes and their values are in the same order as in M.

def stock_list(listOfArt, listOfCat):
    if listOfArt == [] or listOfCat == []:
        return ''
    # Split the code & quantity of books from string to list.
    N = [listOfArt[j].split(' ') for j in range(len(listOfArt))]
    z = ''
    # Check each category for total quantity of books.
    for i in range(len(listOfCat)):
        x = 0
        # Check each book of the book list.
        for k in N:
            if k[0][0] == listOfCat[i]:
                x = x + int(k[1])
        # Prepare the output string.
        z = z + ('(' + listOfCat[i] + ' : ' + str(x) + ')')
        if i < len(listOfCat) - 1:
            z = z + (' - ')
    print(z)
    return z

stock_list(["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"])
# Ans: "(A : 200) - (B : 1140)"
