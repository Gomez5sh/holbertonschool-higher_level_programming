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
    url = http://0.0.0.0:5000/search_user
    try:
        res = requests.post(url, data=data)
        data = res.json()
        if data:
            print("[{}] : {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
