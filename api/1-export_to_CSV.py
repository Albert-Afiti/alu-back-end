#!/usr/bin/python3
"""
Script that uses a REST API to export an employee's TODO list data
in CSV format.

Requirements:
- Uses requests module
- Accepts an integer as a parameter (employee ID)
- Exports all tasks owned by this employee into CSV
- Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv

PEP8 Validation:
- Run `pycodestyle 1-export_to_CSV.py` or `flake8 1-export_to_CSV.py`
- Ensure:
  * Imports are alphabetically ordered
  * Line length ≤ 79 characters
  * Two blank lines before top-level functions
  * Proper indentation (4 spaces)
"""

import csv
import requests
import sys


def export_employee_todo_to_csv(employee_id):
    """
    Fetch tasks for a given employee ID and export them to CSV file.
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

    # Export to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    export_employee_todo_to_csv(employee_id)
