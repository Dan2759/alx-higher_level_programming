#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to a URL with
an email parameter and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    DATA = urllib.parse.urlencode({"email": email})
    DATA = DATA.encode('ascii')

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))
