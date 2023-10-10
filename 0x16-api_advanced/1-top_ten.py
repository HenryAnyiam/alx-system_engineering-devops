#!/usr/bin/python3
"""module with functions working with reddit API"""
import requests


def top_ten(subreddit):
    """get first ten hot posts for a given subreddit"""
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    header = {'user-agent': 'my-app/0.0.1'}
    res = requests.get(url, headers=header, allow_redirects=False)
    if res.status_code == 404:
        print('None')
    else:
        data = res.json()
        data = data.get('data')
        if data is None:
            print('None')
            return
        titles = data.get('children')
        length = len(titles)
        if length < 10:
            titles = titles[:length]
        else:
            titles = titles[:10]
        for i in titles:
            print(i.get('data').get('title'))
