#!/usr/bin/python3
"""A Python script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        html = resp.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
