#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response"""
import request
import sys


if __name__:"__main__":
    res = request.get(sys.argv[1])
    code_stat = res.status_code
    if code_stat >= 400:
        print("Error code: {:d}".format(code_stat))
    else:
        print(res.text)
