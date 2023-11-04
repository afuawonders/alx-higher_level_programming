#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

from sys import argv
from requests import post

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) >= 2 else ""
    response = post(url, data={'q': letter})

    content_type = response.headers['content-type']

    if content_type == 'application/json':
        json_data = response.json()
        user_id = json_data.get('id')
        user_name = json_data.get('name')
        if user_id and user_name:
            print("[{}] {}".format(user_id, user_name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
