#!/usr/bin/pytho3
import requests
import sys
import json

def export_to_json(employee_id):
    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Build JSON structure
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks_list}

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_to_json(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
