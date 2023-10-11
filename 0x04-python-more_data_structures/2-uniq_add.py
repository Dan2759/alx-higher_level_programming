#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)."""
    uniq_list = set(my_list)
    n = 0

    for i in uniq_list:
        n += i

    return (n)
