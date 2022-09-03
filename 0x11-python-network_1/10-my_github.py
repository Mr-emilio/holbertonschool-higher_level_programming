#!/usr/bin/python3
"""script that takes your GitHub
credentials (username and password)
and uses the GitHub API to display
your id"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    headers = {'Authorization': 'token ' + argv[2]}
    response = requests.get(url, headers=headers)
    print(response.json().get('id'))
