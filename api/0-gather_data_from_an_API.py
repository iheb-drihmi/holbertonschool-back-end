#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) != 2:
        exit()

    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url).json()

    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 .format(user_id))
    todos = requests.get(todos_url).json()

    completed_tasks = [task.get('title') for task in todos
                       if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))


