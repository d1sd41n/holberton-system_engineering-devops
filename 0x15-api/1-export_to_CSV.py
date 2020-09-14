#!/usr/bin/python3
"""get from from the api and saves it in a csv file"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    u_url = 'https://jsonplaceholder.typicode.com/' + 'users/' + argv[1]
    response = requests.get(u_url)
    user = response.json().get('username')
    t_url = 'https://jsonplaceholder.typicode.com/' + 'todos'
    response = requests.get(t_url)
    todos = []
    for x in response.json():
        if x.get('userId') == int(argv[1]):
            todos.append(x)
    data_colums = ["userId", "name", "completed", "title"]
    with open('{}.csv'.format(argv[1]), 'w') as fil:
        writer = csv.DictWriter(fil, quoting=csv.QUOTE_ALL,
                                fieldnames=data_colums)
        for i in todos:
            i['name'] = user
            del i['id']
            writer.writerow(i)
