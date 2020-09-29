#!/usr/bin/python3
"""a recursive function that queries the Reddit API and
returns a list containing the titles"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """recurse"""
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    head = {'User-agent': 'qwerty'}
    res = requests.get(url, headers=head)
    if res.status_code != 200:
        return 0
    data = res.json().get('data').get('children')
    for i in data:
        hot_list.append(i.get('data').get('title'))

    aux = res.json().get('data').get('after')
    if aux is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
