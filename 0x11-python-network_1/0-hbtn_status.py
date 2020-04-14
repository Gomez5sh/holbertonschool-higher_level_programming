#!/usr/bin/python3
"""Python script that fetches"""
import urllib.request


url = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(url) as response:
    html = response.read()
    print("Body response")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    html = html.decode('utf-8')
    print("\t- utf8 content: {}".format(html))
