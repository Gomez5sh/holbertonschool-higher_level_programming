#!/usr/bin/python3
"""Python script that takes your Github credentials"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        user = sys.argv[1]
        pasword = sys.argv[2]
        res = requests.get("https://api.github.com/users", auth=(user, pasword))
        data = res.json()
        if data:
            print("{}".format(data.get('id')))
        else:
            print("None")
