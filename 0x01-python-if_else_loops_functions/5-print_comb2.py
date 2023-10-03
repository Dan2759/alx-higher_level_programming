#!/usr/bin/python3
# 5-print_comb2.py

"""Print numbers 0 to 99 separated by ,, followed by a space."""
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
