#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a reques
to the URL and displays the body of the response
Manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            the_page = response.read()
        print(the_page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
