#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
