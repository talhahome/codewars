# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.


def make_readable(time):
    HH = str(int(time/3600))
    if len(HH) == 1:
        HH = "0" + HH
    reminder = time%3600
    MM = str(int(reminder/60))
    if len(MM) == 1:
        MM = "0" + MM
    SS = str(reminder%60)
    if len(SS) == 1:
        SS = "0" + SS
    return str(HH) + ":" + str(MM) + ":" + str(SS)


print(make_readable(359999))
