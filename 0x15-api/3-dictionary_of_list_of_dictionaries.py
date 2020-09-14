#!/usr/bin/python3
"""get data and saves it in a json"""
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users'.format(url)).json()
    todo = requests.get('{}/todos'.format(url)).json()
    data = {}
    for i in users:
        data.update({i.get('id'): []})
        for j in todo:
            if j.get('userId') == i.get('id'):
                dict_ = {
                    'task': j.get('title'),
                    'completed': j.get('completed'),
                    'username': i.get('username')}
                data.get(i.get('id')).append(dict_)
    with open('todo_all_employees.json', "w") as fil:
        json.dump(data, fil)
