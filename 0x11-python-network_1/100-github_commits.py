#!/usr/bin/python3
"""
Takes 2 arguments in order to solve this challenge.
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    repo_name = argv[1]
    owner_name = argv[2]
    i = 0

     URL = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name)

    response = get(URL)
    json = response.json()

    for element in json:
        if i > 9:
            break
        sha = element.get('sha')
        author_name = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
        i += 1
