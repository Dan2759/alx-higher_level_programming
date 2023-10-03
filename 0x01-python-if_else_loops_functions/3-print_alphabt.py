#!/usr/bin/python3
#3-print_alphabt.py

"""Print the alphabet in lowercase, except q and e."""
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
