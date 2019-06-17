# A stream of data is received and needs to be reversed.
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)

# should become:
# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)

# The total number of bits will always be a multiple of 8.

# The data is given in an array as such:
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

def data_reverse(data):
    b = int(len(data) / 8)
    x = []
    j = 0
    for i in range(1, b + 1):
        y = data[j:i * 8]
        x.append(y)
        j = j + 8
    z = []
    for k in reversed(x):
        z.append(k)
    v = []
    for l in range(0, len(z)):
        v = v + z[l]
    return v