#!/usr/bin/python3
"""Fetches the X-Request-Id from the response header using urllib"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        headers = response.headers

    print(headers.get("X-Request-Id"))
