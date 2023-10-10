#!/usr/bin/python3
"""module with functions working with reddit API"""
import requests


def counting(hot_list, word_list):
    """count the occurence of certain strings in a list of strings"""
    if (word_list is None) or (len(word_list) == 0):
        return
    if (hot_list is None) or (len(hot_list) == 0):
        return
    counts = {}
    for i in word_list:
        counts[i] = 0
    for i in hot_list:
        words = i.upper().split(' ')
        for j in counts:
            counts[j] += words.count(j.upper())
    keys = list(counts.keys())
    length = len(keys) - 1
    i = 0
    while i < length:
        if keys[i].upper() == keys[i + 1].upper():
            counts[keys[i]] += counts[keys[i]]
            del counts[keys[i + 1]]
            i += 1
        i += 1
        if i == (length - 1):
            break
    counts = dict(sorted(counts.items(),
                  key=lambda item: (item[1], item[0]),
                  reverse=True))
    for i in counts:
        if counts[i] != 0:
            print(f"{i}: {counts[i]}")


def count_words(subreddit, word_list, hot_list=[], count=0, after=None):
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
        return counting(hot_list, word_list)
    data = res.json()
    data = data.get('data')
    children = data.get('children')
    titles = [i.get('data').get('title') for i in children]
    hot_list.extend(titles)
    after = data.get('after')
    count += 1
    if (after is None) or (after == ""):
        return counting(hot_list, word_list)
    return count_words(subreddit, word_list, hot_list, count, after)
