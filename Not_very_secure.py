# In this example you have to validate if a user input string is alphanumeric.
# The given string is not nil, so you don't have to check that.
#
# The string has the following conditions to be alphanumeric:
#
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces/underscore

import re

def alphanumeric(string):
    s = re.compile(r'[^0-9a-zA-Z]')
    x = s.search(string)
    if not bool(x):
        print(True)
        return True
    else:
        print(False)
        return True


a = "A1"

alphanumeric(a)

