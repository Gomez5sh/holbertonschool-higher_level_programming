#!/usr/bin/python3
"""Python script that takes your Github credentials"""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 3:
        user = sys.argv[1]
        pasw = sys.argv[2]

    resp = requests.get('https://api.github.com/user', auth=(user, pasw))
    content = resp.json()

    if content:
        print("{}".format(content.get('id')))
    else:
        print("None")
