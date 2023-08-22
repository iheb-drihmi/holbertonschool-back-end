#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""
import requests
import sys

def fetch_employee_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data

def display_progress(employee_name, done_tasks, total_tasks):
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"     {task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todos_data = fetch_employee_data(employee_id)

    employee_name = user_data['name']
    done_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    display_progress(employee_name, done_tasks, total_tasks)




