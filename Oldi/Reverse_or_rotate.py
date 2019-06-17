# The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string)
# of size sz (ignore the last chunk if its size is less than sz).
# If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk;
# otherwise rotate it to the left by one position.
# Put together these modified chunks and return the result as a string.
#
# If
# sz is <= 0 or if str is empty return ""
# sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

def revrot(str, sz):
    if sz <= 0 or str == "":
        print("")
        return ""
    elif sz > len(str):
        print("")
        return ""
    else:
        a = list(str)
        b = int(len(a)/sz)
        x = ''
        for i in range(0,b*sz,sz):
            # Chunks are made #
            b = a[i:i+sz]
            # Set of cubes #
            c = [int(j) ** 3 for j in b]
            d = 0
            print(b)
            # Sum of cubes #
            for k in c:
                d += k ** 3
            # Check if divisible by 2 #
            if d % 2 == 0:
                # Make chunk reverse # DYS #
                z = b[::-1]
                # List converted to string #
                y = ''.join(z)
            else:
                # Rotate chunk left by one position # DYS #
                z = b[1:]+b[:1]
                # List converted to string #
                y = ''.join(z)
            # Join Converted Strings #
            x += y
        return x

revrot("123456987654", 6)
