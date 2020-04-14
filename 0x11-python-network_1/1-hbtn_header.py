#!/usr/bin/python3
"""Python script that takes in a URL"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    html = response.getheader('X-Request-Id')
    print(html)
