#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request as requests

if __name__ == '__main__':
    
    with requests.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        display = """Body response:
        - type: {}
        - content: {}
        - utf8 content: {}""".format(
            type(content),
            content,
            content.decode('utf-8')
        )

        print(display)
