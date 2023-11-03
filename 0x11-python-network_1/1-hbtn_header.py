#!/usr/bin/python3
"""A script that takes in URL, sends a request to the URL
and displays the value of the X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    else:
        print("Usage: ./1-hbtn_header.py <URL>")
