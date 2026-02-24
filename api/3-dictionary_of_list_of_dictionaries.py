#!/usr/bin/python3
"""
Script that uses a REST API to export all employees' TODO list data
in JSON format.

Requirements:
- Uses requests module
- Records all tasks from all employees
- Format: {
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE",
         "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE",
         "completed": TASK_COMPLETED_STATUS},
        ...
    ]
  }
- File name must be: todo_all_employees.json

PEP8 Validation:
- Run `pycodestyle 3-dictionary_of_list_of_dictionaries.py`
  or `flake8 3-dictionary_of_list_of_dictionaries.py`
- Ensure:
  * Imports are alphabetically ordered
  * Line length ≤ 79 characters
  * Two blank lines before top-level functions
  * Proper indentation (4 spaces)
"""

import json
import requests


def export_all_employees_todo_to_json():
    """
    Fetch tasks for all employees and export them to a JSON file.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_url = f"{base_url}/users"
    response_users = requests.get(users_url)
    users = response_users.json()

    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get tasks for this user
        todos_url = f"{base_url}/todos?userId={user_id}"
        response_todos = requests.get(todos_url)
        tasks = response_todos.json()

        task_list = []
        for task in tasks:
            task_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_data[str(user_id)] = task_list

    # Export to JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file)


if __name__ == "__main__":
    export_all_employees_todo_to_json()
