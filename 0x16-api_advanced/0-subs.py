#!/usr/bin/python3
"""counts the subscribers"""
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers"""
    url = 'https://www.reddit.com/r/' + subreddit + "/about.json"
    head = {'User-Agent': "qwerty"}
    res = requests.get(url, headers=head, allow_redirects=False)

    if res.status_code == 200:
    	return res.json().get("data").get("subscribers")
    else:
        return 0
