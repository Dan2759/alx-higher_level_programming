#!/usr/bin/python3
"""
Takes in a URL, sends a request to a URL
and displays the body of the response
"""

import sys
from urllib import request
from urllib import error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
