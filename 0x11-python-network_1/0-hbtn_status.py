#!/usr/bin/python3
"""Script that fetches from a url"""

import urllib.request as request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as url:
        page = url.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
