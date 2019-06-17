# Adding Fractions
# In most languages, division immediately produces decimal values, and therefore,
# adding two fractions gives a decimal result:
# (1/2) + (1/4) #=> 0.75
# But what if we want to be able to add fractions and get a fractional result?
# (1/2) + (1/4) #=> 3/4
#
from fractions import Fraction
def add_fracs(*x):
    if len(x) > 0:
        v = []
        for i in x:
            v.append(Fraction(i))
        return str(sum(v))
    else:
        return ''

add_fracs('-2/3', '5/3', '-4/6') # Ans: '1/3'
