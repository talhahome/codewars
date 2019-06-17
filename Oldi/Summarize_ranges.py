# Given a sorted array of numbers, return the summary of its ranges.
#
# Examples
# summary_ranges([1, 2, 3, 4]) == ["1->4"]
# summary_ranges([1, 1, 1, 1, 1]) == ["1"]
# summary_ranges([0, 1, 2, 5, 6, 9]) == ["0->2", "5->6", "9"]
# summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == ["0->7"]
# summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == ["0->7", "9->10"]
# summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) == ["-2", "0->7", "9->10", "12"]

def summary_ranges(nums):
    if len(nums) == 0:
        return []
    # Eliminate multiple values.
    b = []
    for i in nums:
        if b.count(i) < 1:
            b.append(i)
    b.sort()
    # Find consecutive numbers in the list.
    c = b[:1]
    d = []
    for j in range(1, len(b)):
        if b[j] - b[j - 1] == 1:
            c.append(b[j])
        else:
            d.append(c)
            c = []
            c.append(b[j])
    d.append(c)
    # Make arrays of ranges.
    x = []
    for k in d:
        if len(k) > 1:
            x.append("" + str(k[0]) + "->" + str(k[len(k) - 1]))
        else:
            x.append(str(k[0]))
    print(x)
    return x

summary_ranges([])
