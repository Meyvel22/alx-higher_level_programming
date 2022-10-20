#!/bin/bash
# script that sends a request to URL passed as an arg displays only status code
curl -s -w "%{http_code}" "$1" -o /dev/null
