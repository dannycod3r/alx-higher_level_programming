#!/usr/bin/python3
"""Module supplies function to create an object 
using a json file"""
import json


def load_from_json_file(filename):
    """function creates an Object using a JSON file
    
    Args: 
        filename: json file"""
    # load the json, use json.load, loads = load string
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        return data
    