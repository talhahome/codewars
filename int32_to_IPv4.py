# Take the following IPv4 address: 128.32.10.1
#
# This address has 4 octets where each octet is a single byte (or 8 bits).
#
# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
#
# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361
#
# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
#
# Examples
# 2149583361 ==> "128.32.10.1"
# 32         ==> "0.0.0.32"
# 0          ==> "0.0.0.0"

def int32_to_ip(int32):
    bin_a = bin(int32)[2:].zfill(32)
    list_a = [bin_a[i:i + 8] for i in range(0, 31, 8)]
    z = [str(int(i, base=2)) for i in list_a]
    print('.'.join(z))
    return '.'.join(z)

int32_to_ip(2149583361)
