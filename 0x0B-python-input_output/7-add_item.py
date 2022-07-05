#!/usr/bin/python3
"""module"""

import sys


file = "add_item.json"


if __name__ == "__main__":
    save_js = __import__('5-save_to_json_file').save_to_json_file
    load_js = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_js(file)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_js(items, file)
