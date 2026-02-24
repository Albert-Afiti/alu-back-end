#!/usr/bin/python3
"""
Script that uses a REST API to export an employee's TODO list data
in JSON format.

Requirements:
- Uses requests module
- Accepts an integer as a parameter (employee ID)
- Exports all tasks owned by this employee into JSON
- Format: { "USER_ID": [
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
     "username": "USERNAME"},
    ...
  ]}
- File name must be: USER_ID.json

PEP8 Validation:
- Run `pycodestyle 2-export_to_JSON.py` or `flake8 2-export_to_JSON.py`
- Ensure:
  * Imports are alphabetically ordered
  * Line length ≤ 79 characters
  * Two blank lines before top-level functions
  * Proper indentation (4 spaces)
"""

import json
import requests
import sys


def export_employee_todo_to_json(employee_id):
    """
    Fetch tasks for a given employee ID and export them to JSON file.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_url = f"{base_url}/users/{employee_id}"
    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print("Error: Employee not found.")
        return

    user_data = response_user.json()
    username = user_data.get("username")

    # Get employee's tasks
    todos_url = f"{base_url}/todos?userId={employee_id}"
    response_todos = requests.get(todos_url)
    tasks = response_todos.json()

    # Build JSON structure
    task_list = []
    for task in tasks:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): task_list}

    # Export to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    export_employee_todo_to_json(employee_id)
