#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the variable
X-Request-Id in the response header.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
