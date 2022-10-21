#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rq = requests.get(url)
    if rq.status_code >= 400:
        print("Error code: {}".format(rq.status_code))
    else:
        print(rq.text)
