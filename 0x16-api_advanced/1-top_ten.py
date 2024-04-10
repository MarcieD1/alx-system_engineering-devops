#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Read reddit API and print titles of the first 10 hot posts"""
    headers = {'User-Agent': 'My User Agent 1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print('None')
        else:
            print(f"Error: {err}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
