#!/bin/bash
# Bash script that displays the status code of request
curl -so /dev/null -w "%{http_code}" "$1"
