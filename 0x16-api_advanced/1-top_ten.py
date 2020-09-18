#!/usr/bin/python3
"""queries the Reddit API and prints the titles
of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """top_ten"""
    url = 'https://www.reddit.com/r/' + subreddit + "/hot.json"
    head = {'User-Agent': 'qwerty'}
    res = requests.get(url, headers=head, allow_redirects=False)
    if res.status_code == 200:
        JSON__ = res.json()
        if 'data' in JSON__:
            for post_res in JSON__.get("data").get("children"):
                print(post_res.get("data").get("title"))
        else:
            print(None)
    else:
        print(None)
        return 0
