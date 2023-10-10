#!/usr/bin/python3
"""module with fucvtion to access the REDDIT API"""
import requests


def number_of_subscribers(subreddit):
    """provide the number of subscriber to a subreddit"""
    headers = {'user-agent': 'my-app/0.0.1'}
    url = f"https://api.reddit.com/r/{subreddit}/about"
    res = requests.get(url, headers=headers)
    if res.status_code == 404:
        return 0
    data = res.json()
    return data.get('data').get('subscribers')
