#!/usr/bin/python3
"""Sends a POST request with a letter and handles JSON response"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    # If no argument is given → q = ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url, data={"q": q})

    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(0)

    if not data:
        print("No result")
    else:
        print("[{}] {}".format(data.get("id"), data.get("name")))
