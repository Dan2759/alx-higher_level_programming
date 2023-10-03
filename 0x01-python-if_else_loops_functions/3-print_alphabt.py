#!/usr/bin/python3
#3-print_alphabt.py

"""Print all alphabet in lowercase, except q and e."""
for char_code in range(ord('a'), ord('z') + 1):
    if chr(char_code) not in ['q', 'e']:
        print(chr(char_code), end='')
