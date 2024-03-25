#!/usr/bin/python3

import json
import requests

def export_all_tasks_to_json():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    
    if response.status_code == 200:
        todos = response.json()
        all_employees_tasks = {}

        for task in todos:
            user_id = str(task['userId'])
            task_data = {
                "username": task.get('username', 'Unknown'),
                "task": task.get('title', 'Unknown'),
                "completed": task.get('completed', False)
            }

            if user_id in all_employees_tasks:
                all_employees_tasks[user_id].append(task_data)
            else:
                all_employees_tasks[user_id] = [task_data]

        with open("todo_all_employees.json", 'w') as file:
            json.dump(all_employees_tasks, file, indent=4)
    else:
        print("Failed to retrieve data from the API.")

if __name__ == "__main__":
    export_all_tasks_to_json()
