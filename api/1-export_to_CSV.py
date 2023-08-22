#!/usr/bin/python3
"""
Using what you did in the task #0
"""
import csv
import requests
import sys

if __name__ == "__main__":
    """ Gets employee todo information """
    id = sys.argv[1]

    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id).json()
    USERNAME = user_url.get('username')
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id + '/todos')

    with open("{}.csv".format(id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos.json():
            writer.writerow([id, USERNAME, task.get('completed'), task.get('title')])

    print("Data exported to {}.csv".format(id))
