#!/usr/bin/python3
""" Add all arguments to a python list """
import sys


if __name__ == "__main__":
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    try:
        res = load_from_json_file("add_item.json")
    except FileNotFoundError:
        res = []
    res.extend(sys.argv[1:])
    save_to_json_file(res, "add_item.json")