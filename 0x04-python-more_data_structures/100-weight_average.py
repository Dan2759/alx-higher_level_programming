#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple."""
    if not my_list:
        return 0

    n = 0
    den = 0

    for tup in my_list:
        n += tup[0] * tup[1]
        den += tup[1]

    return (n / den)
