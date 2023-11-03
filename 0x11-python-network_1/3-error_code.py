#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

import sys
import urllib.error
import urllib.request

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
