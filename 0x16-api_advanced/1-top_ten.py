#!/usr/bin/python3
"""
Function prints the titles of the first 10 hot
posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot
    posts listed for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        print("None")
        return
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        'User-Agent': 'test'
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for res in results.get("children"):
        print(res.get("data").get("title"))
