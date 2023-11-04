#!/usr/bin/python3

# A Python script that takes 2 arguments in order to solve a challenge.

import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    m = requests.get(url)
    commits = m.json()
    try:
        for i in range(10):
            print(f"{commits[i]['sha']}:
                    {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
