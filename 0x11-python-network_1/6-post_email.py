#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

from sys import argv
from requests import post

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    res = post(url, {'email': email})
    print(res.text)
