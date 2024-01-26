#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    r = requests.get(url)
    x = r.text
    body = response.read()
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
