#!/usr/bin/python3
"""Python script that takes in a URL
sends a request to the URL and displays """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    resp = r.headers.get('X-Request-Id')

    print(resp)
