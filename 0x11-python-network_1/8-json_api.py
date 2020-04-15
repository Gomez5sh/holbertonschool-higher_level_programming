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
        id = data.get('id')
        name = data.get('name')

        if id and name is None:
            print("No result")
        else:
            print("[{}] : {}".format(id, name))
    except:
        print("Not a valid JSON")
