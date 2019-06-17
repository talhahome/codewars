# You will be given a number and you will need to return it as a string in Expanded Form. For example:
# expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
# expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
# expanded_form(0.04) # Should return '4/100'

import decimal
def expanded_form(num):
    q = decimal.Decimal(str(num))
    r = q.as_tuple().exponent
    # Number of digits after decimal
    # n = abs(r)
    # Digits after decimal
    after = str(num)[r:]
    # Number of digits before decimal
    m = len(str(num)) - (abs(r)+1)
    # Digits before decimal
    before = str(num)[:len(str(num)) - (abs(r)+1)]
    z = ''
    # For digits before decimal
    for i in str(before):
        m = m-1
        if i != '0':
            z = z + str(int(i) * (10 ** m)) + ' + '
    # For digits after decimal
    count = 1
    for j in str(after):
        if j != '0':
            z = z + str(j) + '/' + str(10 ** count) + ' + '
        count = count + 1
    print(z[:-3])

expanded_form(693.230459)
# Ans: '600 + 90 + 3 + 2/10 + 3/100 + 4/10000 + 5/100000 + 9/1000000'

# expanded_form(1.24)
# Ans: '1 + 2/10 + 4/100'

# expanded_form(7.304)
# Ans: '7 + 3/10 + 4/1000'

# expanded_form(0.004)
# Index out of range problem.
