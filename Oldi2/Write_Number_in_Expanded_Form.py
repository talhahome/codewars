# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    z = ''
    while len(str(num)) > 1:
        x = num % 10**(len(str(num))-1)
        z = z + str(num - x) + ' + '
        num = x
    if num != 0:
        z = z + str(num)
    else:
        z = z[:-3]
    print(z)
    return z

expanded_form(70304)
# Ans: '70000 + 300 + 4'
