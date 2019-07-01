# The rgb() method is incomplete. Complete the method
# so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# The valid decimal values for RGB are 0 - 255.
# Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3
import re


def rgb(r, g, b):
    if 0 > r:
        r = 0
    elif r > 255:
        r = 255
    if 0 > g:
        g = 0
    elif g > 255:
        g = 255
    if 0 > b:
        b = 0
    elif b > 255:
        b = 255
    r = re.sub(r'0x', '', hex(r))
    g = re.sub(r'0x', '', hex(g))
    b = re.sub(r'0x', '', hex(b))
    if len(r) == 1:
        r = "0" + r
    if len(g) == 1:
        g = "0" + g
    if len(b) == 1:
        b = "0" + b
    print(r.upper() + "" + g.upper() + "" + b.upper())


# rgb(255, 255, 255)
# rgb(255, 255, 300)
# rgb(0, 0, 0)
# rgb(148, 0, 211)
rgb(-20,275,125)

