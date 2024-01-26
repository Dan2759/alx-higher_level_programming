#!/usr/bin/python3
"""
Takes 2 arguments in order to solve this challenge.
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    i = 0

     URL = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = get(URL)
    json = response.json()

    for element in json:
        if i > 9:
            break
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1
