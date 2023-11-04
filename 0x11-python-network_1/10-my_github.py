#!/usr/bin/python3
"""A Python script that takes your GitHub credentials(username and password)
and uses the GitHub API to display your id"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    data_result = requests.get(url, auth=(user, passwd))

    try:
        data_json = data_result.json()
        print(data_json["id"])
    except Exception:
        print("None")
