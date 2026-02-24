#!/usr/bin/python3
import requests
import json

def export_all_to_json():
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to hold all employees' tasks
    all_tasks = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch todos for this user
        todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Build list of tasks for this user
        tasks_list = []
        for task in todos_data:
            tasks_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        # Add to dictionary
        all_tasks[str(user_id)] = tasks_list

    # Write to JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(all_tasks, json_file)

if __name__ == "__main__":
    export_all_to_json()
