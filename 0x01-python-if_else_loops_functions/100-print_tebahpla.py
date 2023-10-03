#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating lowercaseand uppercase
(z in lowercase and Y in uppercase) , not followed by a new line."""
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
