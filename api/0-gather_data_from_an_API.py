#!/usr/bin/python3
import requests
import sys

def get_todo_progress(employee_id):
    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = reques#!/usr/bin/python3
"""
Script to fetch and display TODO list progress for a given employee ID
using the JSONPlaceholder REST API.
"""

import requests
import sys


def get_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee
    """
    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if not user_data or "name" not in user_data:
        print("Employee not found.")
        return

    employee_name = user_data.get("name")

    # Fetch todos for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    # Print progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")ts.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    # Print progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
