#!/usr/bin/env python3
"""Script that displays GitHub user location or rate limit status"""
import sys
import requests
from datetime import datetime


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 403:
        reset_time = int(response.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(datetime.now().timestamp())
        minutes_remaining = (reset_time - current_time) // 60
        print(f"Reset in {minutes_remaining} min")
    elif response.status_code == 404:
        print("Not found")
    else:
        data = response.json()
        print(data.get('location', ''))
