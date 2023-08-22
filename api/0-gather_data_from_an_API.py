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
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Error fetching user data.")
        exit()

    user = user_response.json()

    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Error fetching user's tasks.")
        exit()

    todos = todos_response.json()

    completed_tasks = [task.get('title') for task in todos if task.get('completed') is True]
    print(f"Employee {user.get('name')} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t{task}")




