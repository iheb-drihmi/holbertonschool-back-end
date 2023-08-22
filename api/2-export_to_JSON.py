#!/usr/bin/python3
"""
Export to JSON
"""
import requests
import sys
import json

if __name__ == "__main__":
    """ Gets employee info in json format """
    id = sys.argv[1]
    tasks = []

    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + id).json()

    for task in todos:
        task_data = {
            'task': task['title'],
            'completed': task['completed'],
            'username': user_url['username']
        }
        tasks.append(task_data)
    data = {id: tasks}

    with open(id + '.json', 'w') as f:
        json.dump(data, f)
