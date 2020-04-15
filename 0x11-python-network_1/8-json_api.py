#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
"""
import requests
import sys


if __name__ == "__main__":
    try:
        rep = sys.argv[1]
    except:
        rep = ""

    data = {'q': rep}
    url = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        data = url.json()
        if data:
            print("[{}] : {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
