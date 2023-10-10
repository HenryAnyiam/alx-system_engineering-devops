#!/usr/bin/python3
"""module with functions working with reddit API"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """het all the titles of a subreddit hot topics"""
    headers = {'user-agent': 'my-app/0.0.1'}
    if count == 0:
        url = f"https://api.reddit.com/r/{subreddit}/hot"
    else:
        url = f"https://api.reddit.com/r/{subreddit}/hot"
        url += f"?after={after}&count={count}"
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        if len(hot_list) == 0:
            return None
        return hot_list
    data = res.json()
    data = data.get('data')
    children = data.get('children')
    titles = [i.get('data').get('title') for i in children]
    hot_list.extend(titles)
    after = data.get('after')
    count += 1
    if (after is None) or (after == ""):
        return hot_list
    return recurse(subreddit, hot_list, count, after)
