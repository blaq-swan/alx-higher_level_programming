#!/usr/bin/python3
"""
sends a POST resquestr to a URL with an email
"""

import sys
import urllib as url


if __name__ == "__main__":
    link = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = url.parse.urlencode(email).encode("ascii")

    request = url.request.Request(link, data)
    with url.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
