#!/usr/bin/python3

import json
import requests
import sys

def export_to_json(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        todos = response.json()
        file_name = f"{employee_id}.json"

        data = {str(employee_id): []}
        for task in todos:
            task_data = {
                "task": task.get('title', 'Unknown'),
                "completed": task.get('completed', False),
                "username": task.get('username', 'Unknown')
            }
            data[str(employee_id)].append(task_data)

        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
