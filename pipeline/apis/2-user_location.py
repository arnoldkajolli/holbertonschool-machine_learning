#!/usr/bin/env python3
"""Script that displays user location from an API"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
        
    url = sys.argv[1]
    response = requests.get(url).json()
    print(response.get('location', ''))
