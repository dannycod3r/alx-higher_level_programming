#!/bin/bash
# A script that send json data and displays the response
curl -s -X POST -H "Content-type: application/json" -d "$(cat "$2")" "$1"
