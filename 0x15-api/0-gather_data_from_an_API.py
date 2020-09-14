#!/usr/bin/python3
"""get text fom the api"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(url, argv[1]))
    res = requests.get('{}/todos?userId={}'.format(url, argv[1]))
    tks = len([x for x in res.json() if x.get('completed') is True])
    print('Employee {} is done with tasks({}/{}):'
          .format(user.json().get('name'), tks, len(res.json())))
    for i in res.json():
        if i.get('completed') is True:
            print('\t {}'.format(i.get('title')))
