#!/usr/bin/python3
"""
Script that uses a REST API to return information about an employee's
TODO list progress.

Requirements:
- Uses requests module
- Accepts an integer as a parameter (employee ID)
- Displays employee TODO list progress in the specified format

PEP8 Validation:
- Run `pycodestyle 0-gather_data_from_an_API.py` or `flake8 0-gather_data_from_an_API.py`
- Ensure:
  * Imports are alphabetically ordered
  * Line length ≤ 79 characters
  * Two blank lines before top-level functions
  * One blank line between logical code sections inside functions
  * Proper indentation (4 spaces)
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display TODO list progress for a given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_url = f"{base_url}/users/{employee_id}"
    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print("Error: Employee not found.")
        return

    employee_name = response_user.json().get("name")

    # Get employee's tasks
    todos_url = f"{base_url}/todos?userId={employee_id}"
    response_todos = requests.get(todos_url)
    tasks = response_todos.json()

    # Calculate progress
    total_tasks = len(tasks)
    done_tasks = [task for task in tasks if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print progress
    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
