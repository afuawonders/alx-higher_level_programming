#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a
POST request to the passed URL"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
