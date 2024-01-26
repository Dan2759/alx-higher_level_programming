#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        body = response.read()
        print(f"Body response:")
        print(f"\t- type: {}".format(type(body)))
        print(f"\t- content: {}".format(body))
        print(f"\t- utf8 content: {}".format(body.decode('utf-8')))
