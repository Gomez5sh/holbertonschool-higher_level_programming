#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    code_stat = res.status_code
    if code_stat >= 400:
        print("Error code: {}".format(code_stat))
    else:
        print(res.text)
