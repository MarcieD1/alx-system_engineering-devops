#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys

def top_ten(subreddit):
    """Read reddit API and return top 10 hotspots """
    headers = {'user-agent': '/u/Ok_Internet3066 ALX APP for holberton school'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data")
        if data and "children" in data:
            children = data["children"]
            for child in children[:10]:
                print(child["data"]["title"])
        else:
            print("No posts found in subreddit: {}".format(subreddit))
    elif response.status_code == 404:
        print("Subreddit '{}' not found.".format(subreddit))
    else:
        print("Error fetching data. Status code: {}".format(response.status_code))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a subreddit name.")
        sys.exit(1)

    subreddit = sys.argv[1]
    top_ten(subreddit)
