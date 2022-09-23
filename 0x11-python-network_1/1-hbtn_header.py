#!/usr/bin/python3
"""Shows the X-Request-Id of a request from a URL"""

import urllib.request as request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    query = request.Request(url)
    with request.urlopen(query) as page:
        print(dict(page.headers).get("X-Request-Id"))
