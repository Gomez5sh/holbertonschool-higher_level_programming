#!/usr/bin/python3
"""Python script that takes your Github credentials"""
import requests
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    res = requests.get("https://api.github.com/user",
                     auth=(sys.argv[1], sys.argv[2]))
    payload = res.json()
    id = payload.get('id')
    print(id)
